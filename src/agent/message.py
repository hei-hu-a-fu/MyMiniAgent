class Message:
    def __init__(self, content, role):
        self.content = content
        self.role = role

class Memory:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

    def clear_memory(self):
        self.messages = []

    def get_last_message(self):
        if self.messages:
            return self.messages[-1]
        return None