# dynamic_scheduler.py

from typing import List, Dict

def schedule_tasks(tasks: List[Dict], resources: Dict) -> List[Dict]:
    """
    Schedule tasks dynamically based on available resources.

    Args:
        tasks (List[Dict]): A list of tasks, each represented as a dictionary.
        resources (Dict): A dictionary of available resources.

    Returns:
        List[Dict]: List of scheduled tasks with resource allocation.
    """
    scheduled_tasks = []

    for task in tasks:
        required_resource = task.get("resource")
        if required_resource and resources.get(required_resource, 0) > 0:
            # Allocate resource to the task
            resources[required_resource] -= 1
            task["status"] = "Scheduled"
            scheduled_tasks.append(task)
        else:
            task["status"] = "Pending"

    return scheduled_tasks

if __name__ == "__main__":
    # Example usage
    tasks = [
        {"id": 1, "name": "Task A", "resource": "CPU"},
        {"id": 2, "name": "Task B", "resource": "GPU"},
        {"id": 3, "name": "Task C", "resource": "CPU"},
    ]
    resources = {"CPU": 1, "GPU": 1}

    scheduled = schedule_tasks(tasks, resources)
    print("Scheduled Tasks:", scheduled)
