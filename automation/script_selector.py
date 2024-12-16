import os
from typing import List

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
        return [file for file in os.listdir(directory) if file.endswith('.py')]
    except FileNotFoundError:
        return []

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