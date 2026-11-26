from src.agent.agent import Agent
from src.agent.model import LLMModel
from src.agent.model import ModelManager
from src.agent.message import Memory, Message
from src.chatbot.diagnosis import Diagnosis

class ChatBotAgent(Agent):
    def __init__(self, name = "ChatBot", description = "A simple chatbot agent", env = None, tools = None, model = None, model_name = None):
        super().__init__(name, description, env, tools, model)
        self.Diagnosis = Diagnosis()  # Initialize Diagnosis attribute
        self.Memory = self.Diagnosis.Memory  # Initialize Memory attribute
        self.model_name = model_name
        self.model= ModelManager().get_model(model_name=model_name)  # Initialize model attribute with the specified model
        


    def request_agent(self, request_model_name=None):
        if request_model_name == self.model_name:
            
            prompt = self.Memory.get_current_context(self.Memory.Window_size)
            self.agent_loop(prompt, self.Memory)
        else:
            print(f"exchange to {request_model_name} ")
            self.model_name = request_model_name
            self.model = ModelManager().get_model(model_name=request_model_name)
            prompt = self.Memory.get_current_context(self.Memory.Window_size)
            self.agent_loop(prompt, self.Memory)
            

    def quit(self):
        # Save the current memory to a file before quitting
        self.Diagnosis.save_memory_to_file(f"{self.Diagnosis.id}_diagnosis_log.txt")

