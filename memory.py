from collections import deque

class ConversationMemory:
    def __init__(self, window_size: int = 10) -> None:
        self.window_size = window_size
        self.messages = deque(maxlen=window_size)

    def add_user_message(self, message: str) -> None:
        self.messages.append({"role": "user", "content": message})

    def add_ai_message(self, message: str) -> None:
        self.messages.append({"role": "assistant", "content": message})

    def get_messages(self) -> list[dict[str, str]]:
        return list(self.messages)

    def clear(self) -> None:
        self.messages.clear()
