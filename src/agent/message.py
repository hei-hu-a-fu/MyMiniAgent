class Message:
    def __init__(self, content, role):
        self.content = content
        self.role = role

class Memory:
    def __init__(self, max_size, window_size):
        self.messages = []
        self.MAX_MEMORY_SIZE = max_size  # Maximum number of messages to store
        self.Window_size = window_size  # Number of messages to show to agent in a window,latest messages will be shown to agent
        self.Current_memory_size = 0  # Current number of messages stored in memory


    def add_message(self, message):
        if self.Current_memory_size >= self.MAX_MEMORY_SIZE:
            # Remove the oldest message to make space for the new one
            self.messages.pop(0)
            self.Current_memory_size -= 1
        self.messages.append(message)
        self.Current_memory_size += 1

    def get_all_messages(self):
        return self.messages

    def clear_memory(self):
        self.messages = []

    def get_last_message(self):
        if self.messages:
            return self.messages[-1]
        return None

    def current_context(self, context_size):
        if context_size <= 0:
            return []
        return self.messages[-context_size:]