from src.agent.message import Memory, Message
import random
from datetime import datetime

class Diagnosis:
    def __init__(self, memory=None):
        self.id = self.initialize_id()
        self.Memory = memory if memory is not None else memory(max_size=100,window_size=20)  # Initialize memory attribute
        self.context = memory.get_current_context(self.Memory.Window_size)  # Initialize context attribute
        self.saved_memory = 0

    def initialize_id(self):
        # Initialize the diagnosis ID with a random number for demonstration purposes
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        random_num = random.randint(1000, 9999)

        return f"diagnosis_{timestamp}_{random_num}"

    def get_context(self):
        return self.context

    def add_message(self, message, message_role:str=None):
        self.Memory.add_message(Message(content=message, role=message_role))
        self.write_message_to_file(message)
        self.context = self.Memory.get_current_context(self.Memory.Window_size)  # Update context after adding a new message

    def write_message_to_file(self, message):
        filename=f"{self.id}_diagnosis_log.txt"  #change to jsonl

        with open(filename, "a") as file:
            file.write(f"{datetime.now()}: {message}\n")

    def diagnosis_initialize_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    # Assuming the log format is: "timestamp: message"
                    timestamp, message = line.strip().split(": ", 1)
                    self.Memory.add_message(Message(content=message, role="assistant"))  # Assuming role is assistant for logged messages
            self.context = self.Memory.get_current_context(self.Memory.Window_size)  # Update context after loading messages
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty diagnosis.")

    def save_memory_to_file(self, filename):
        """
        Save the current memory messages to a file.

        """
        if self.Memory.Current_memory_size - self.saved_memory >=0:
            with open(filename, "a") as file:
                        for i in range(self.saved_memory, self.Memory.Current_memory_size):
                            message = self.Memory.messages[i]
                            file.write(f"{datetime.now()}: {message.role}: {message.content}\n")
            self.saved_memory = self.Memory.Current_memory_size
        else:
            print("No new messages to save.")
            return
        