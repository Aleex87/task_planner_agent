def create_task_list(goal: str) -> list[str]:
    """
    Generate a list of tasks from a user goal.
    """

    goal_lower = goal.lower()

    if "study" in goal_lower or "exam" in goal_lower:
        return [
            "Define what you need to study",
            "Collect study materials",
            "Break the subject into smaller topics",
            "Create a study schedule",
            "Review progress regularly",
            "Test yourself with practice questions",
        ]

    if "project" in goal_lower:
        return [
            "Define the project goal",
            "List the main requirements",
            "Break the work into smaller tasks",
            "Set priorities",
            "Create a timeline",
            "Review and adjust the plan",
        ]

    if "learn" in goal_lower:
        return [
            "Define what you want to learn",
            "Find beginner-friendly resources",
            "Break the topic into small parts",
            "Practice consistently",
            "Track your progress",
            "Review weak areas",
        ]

    return [
        "Define the goal clearly",
        "Break the goal into smaller tasks",
        "Order the tasks logically",
        "Start with the first small action",
        "Review progress and adjust if needed",
    ]


def prioritize_tasks(tasks: list[str]) -> list[str]:
    """
    Order tasks based on simple priority rules.
    """

    priority_keywords = [
        "define",
        "collect",
        "list",
        "break",
        "create",
        "start",
        "review",
        "test",
    ]

    def task_priority(task: str) -> int:
        task_lower = task.lower()
        for index, keyword in enumerate(priority_keywords):
            if keyword in task_lower:
                return index
        return len(priority_keywords)

    return sorted(tasks, key=task_priority)
