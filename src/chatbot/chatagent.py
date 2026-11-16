from src.agent import Agent
class ChatBotAgent(Agent):
    def __init__(self, name = "ChatBot", description = "A simple chatbot agent", env = None, tools = None, model = None):
        super().__init__(name, description, env, tools, model)

    def respond(self, message):
        # Simple response logic for demonstration purposes
        return f"{self.name} says: I received your message: '{message}'"