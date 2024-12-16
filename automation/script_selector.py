import os
import subprocess
from typing import List, Tuple

def select_script(scripts: List[str], criteria: str) -> str:
    """
    Select a script based on given criteria.

    Args:
        scripts (List[str]): A list of script names.
        criteria (str): The selection criteria.

    Returns:
        str: The selected script name.
    """
    for script in scripts:
        if criteria in script:
            return script
    return ""

def list_available_scripts(directory: str) -> List[str]:
    """
    List all scripts in the given directory.

    Args:
        directory (str): The path to the directory.

    Returns:
        List[str]: A list of script names.
    """
    try:
        files = os.listdir(directory)
        print(f"Debug: Files in '{directory}': {files}")
        return [file for file in files if file.endswith('.py')]
    except FileNotFoundError:
        print(f"Debug: Directory '{directory}' not found.")
        return []


def execute_script_safe(script_path: str, commands: List[str]) -> Tuple[str, str]:
    """
    Execute a script safely and capture its output and error.

    Args:
        script_path (str): Path to the script to execute.
        commands (List[str]): Additional commands or arguments to pass.

    Returns:
        Tuple[str, str]: A tuple of (stdout, stderr) outputs from the execution.
    """
    try:
        result = subprocess.run(
            ["python", script_path, *commands],
            capture_output=True,
            text=True
        )
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)

if __name__ == "__main__":
    # Example usage
    scripts_directory = "./automation"
    criteria = "executor"

    print("Listing available scripts...")
    scripts = list_available_scripts(scripts_directory)
    print("Available scripts:", scripts)

    print("Selecting script based on criteria...")
    selected_script = select_script(scripts, criteria)
    print("Selected script:", selected_script)