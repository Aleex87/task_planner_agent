from agent import TaskPlannerAgent
from util.pretty_print import print_welcome, get_user_input, print_goodbye
from util.streaming_utils import handle_stream


def main() -> None:
    print_welcome(
        title="Task Planner Agent",
        description=(
            "This agent helps you break down goals into actionable plans.\n"
            "Type 'exit' or 'quit' to stop the program."
        ),
    )

    agent = TaskPlannerAgent()

    while True:
        user_input = get_user_input(prompt="Enter your goal")

        if not user_input or user_input.lower() in {"exit", "quit"}:
            print_goodbye("Exiting Task Planner Agent...")
            break

        final_response = handle_stream(agent.stream(user_input))

        
        if final_response:
            agent.save_conversation(user_input, final_response)


if __name__ == "__main__":
    main()
    