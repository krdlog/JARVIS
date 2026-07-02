from collections import deque


class Conversation:

    def __init__(self):

        self.history = deque(maxlen=20)

    def add(self, role, message):

        self.history.append(
            {
                "role": role,
                "content": message
            }
        )

    def messages(self):

        return list(self.history)

    def clear(self):

        self.history.clear()