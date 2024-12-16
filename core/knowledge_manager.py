# knowledge_manager.py

from typing import List, Any, Dict

def extract_knowledge(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Extract relevant knowledge from a dataset.

    Args:
        data (List[Dict[str, Any]]): The dataset containing information.

    Returns:
        Dict[str, Any]: Extracted knowledge in structured form.
    """
    knowledge = {}

    for entry in data:
        topic = entry.get("topic")
        details = entry.get("details")

        if topic and details:
            if topic not in knowledge:
                knowledge[topic] = []
            knowledge[topic].append(details)

    return knowledge

def merge_knowledge(bases: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Merge multiple knowledge bases into one.

    Args:
        bases (List[Dict[str, Any]]): List of knowledge bases to merge.

    Returns:
        Dict[str, Any]: A unified knowledge base.
    """
    unified_knowledge = {}

    for base in bases:
        for topic, details in base.items():
            if topic not in unified_knowledge:
                unified_knowledge[topic] = []
            unified_knowledge[topic].extend(details)

    return unified_knowledge

if __name__ == "__main__":
    # Example usage
    dataset = [
        {"topic": "AI", "details": "Artificial Intelligence overview."},
        {"topic": "AI", "details": "Applications of AI in industry."},
        {"topic": "Cloud", "details": "Cloud computing basics."},
    ]

    base1 = {"AI": ["Deep learning techniques."], "Cloud": ["Serverless architecture."]}
    base2 = {"AI": ["Reinforcement learning."], "Data": ["Big Data analytics."]}

    extracted = extract_knowledge(dataset)
    merged = merge_knowledge([base1, base2, extracted])

    print("Extracted Knowledge:", extracted)
    print("Merged Knowledge Base:", merged)
