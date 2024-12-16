# main.py
from flask import Flask, request, jsonify
from core.goal_optimizer import optimize_goals
from knowledge_modules.llm_knowledge import extract_knowledge
from automation.script_selector import execute_script_safe

app = Flask(__name__)

@app.route('/')
def home():
    """Root endpoint."""
    return "Welcome to AGI Project!"

@app.route('/tasks', methods=['POST'])
def handle_tasks():
    """Interact with AGI to prioritize tasks."""
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request data"}), 400
        tasks = data.get("tasks", [])
        completed = data.get("completed", [])
        if not tasks:
            return jsonify({"error": "Tasks list cannot be empty"}), 400
        optimized_tasks = optimize_goals(tasks, completed)
        return jsonify(optimized_tasks)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/knowledge', methods=['POST'])
def fetch_knowledge():
    """Fetch knowledge using LLMs."""
    try:
        query = request.json.get("query")
        if not query:
            return jsonify({"error": "No query provided"}), 400
        knowledge = extract_knowledge(query)
        return jsonify({"knowledge": knowledge})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/execute', methods=['POST'])
def execute_script():
    """Execute a specified script."""
    try:
        script_type = request.json.get("script_type")
        commands = request.json.get("commands", [])
        if not script_type or not commands:
            return jsonify({"error": "Script type and commands are required"}), 400
        result = execute_script_safe(script_type, commands)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/status', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "Running", "version": "1.0.0"}), 200

if __name__ == '__main__':
    app.run(debug=True)