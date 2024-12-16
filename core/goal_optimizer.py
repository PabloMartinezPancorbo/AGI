# goal_optimizer.py

from typing import List

def optimize_goals(goals: List[str], completed: List[str]) -> List[str]:
    """
    Optimize and prioritize goals based on completion status.

    Args:
        goals (List[str]): List of goals to optimize.
        completed (List[str]): List of completed goals.

    Returns:
        List[str]: Optimized list of remaining goals.
    """
    remaining_goals = [goal for goal in goals if goal not in completed]
    return sorted(remaining_goals)

def prioritize_goals(goals: List[str], priority_keywords: List[str]) -> List[str]:
    """
    Prioritize goals based on given keywords.

    Args:
        goals (List[str]): List of goals to prioritize.
        priority_keywords (List[str]): Keywords to prioritize goals.

    Returns:
        List[str]: Goals sorted by priority.
    """
    prioritized = sorted(goals, key=lambda goal: any(keyword in goal for keyword in priority_keywords), reverse=True)
    return prioritized

if __name__ == "__main__":
    # Example usage
    goals = ["Finish project report", "Prepare presentation", "Update software", "Team meeting"]
    completed = ["Team meeting"]
    priority_keywords = ["project", "presentation"]

    optimized = optimize_goals(goals, completed)
    prioritized = prioritize_goals(optimized, priority_keywords)

    print("Optimized Goals:", optimized)
    print("Prioritized Goals:", prioritized)