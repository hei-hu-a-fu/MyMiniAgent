from src.agent import Agent
from src.chatbot.diagnosis import Diagnosis
class ChatBotAgent(Agent):
    def __init__(self, name = "ChatBot", description = "A simple chatbot agent", env = None, tools = None, model = None):
        super().__init__(name, description, env, tools, model)
        self.Diagnosis = Diagnosis(self.model, self)  # Initialize diagnosis attribute

    def respond(self, message):
        # Simple response logic for demonstration purposes
        return f"{self.name} says: I received your message: '{message}'"

    def user_request_model(self, model, prompt):
        # Create a new Diagnosis instance with the provided model
        response = self.model.generate_response(prompt)
        self.Diagnosis.add_message(response)
        return response