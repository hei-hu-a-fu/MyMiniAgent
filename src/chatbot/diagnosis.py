from src.agent.message import Message
import random
from datetime import datetime

class Diagnosis:
    def __init__(self, model, ChatBotAgent):
        self.id = self.initialize_id()
        self.model = model
        self.messages: list[Message] = []

    def initialize_id(self):
        # Initialize the diagnosis ID with a random number for demonstration purposes
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        random_num = random.randint(1000, 9999)

        return f"diagnosis_{timestamp}_{random_num}"

    def exchange_model(self, model: str):
        self.model = model
