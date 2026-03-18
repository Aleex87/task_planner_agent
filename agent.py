from langchain.agents import create_agent

from memory import ConversationMemory
from prompts import get_system_prompt
from tools import create_task_list, prioritize_tasks
from util.models import get_model
from util.streaming_utils import STREAM_MODES


class TaskPlannerAgent:
    def __init__(self) -> None:
        self.memory = ConversationMemory(window_size=10)

        self.model = get_model(
            temperature=0.7,
            top_p=0.9,
        )

        self.agent = create_agent(
            model=self.model,
            tools=[create_task_list, prioritize_tasks],
            system_prompt=get_system_prompt(),
        )

    def _build_messages(self, user_input: str) -> list[dict[str, str]]:
        messages = self.memory.get_messages().copy()
        messages.append({"role": "user", "content": user_input})
        return messages

    def stream(self, user_input: str):
        messages = self._build_messages(user_input)

        return self.agent.stream(
            {"messages": messages},
            stream_mode=STREAM_MODES,
        )

    def save_conversation(self, user_input: str, agent_output: str) -> None:
        self.memory.add_user_message(user_input)
        self.memory.add_ai_message(agent_output)
