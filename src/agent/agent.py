from message import Memory, Message
from src.agent import model

class Agent:
    def __init__(self, name, description, env, tools , local_model):
        self.name = name
        self.description = description
        self.model: model.LLMModel = local_model
        self.tools = tools
        self.environment = env

    def agent_loop(self, user_input, Memory:Memory):
        Memory.add_message(Message(content=user_input, role="user"))
        while True:
            # Get the current context from memory
            current_context = Memory.get_current_context(Memory.Window_size)
            prompt = current_context
            response = self.model.generate_response(prompt)
            print(f"Agent response: {response}")
            single_turn_tool_result = []
            if response.tools:
                for tool in response.tools:
                    single_turn_tool_result.append(tool.run())
                Memory.add_message(Message(content=single_turn_tool_result, role="tool"))
            else:
                Memory.add_message(Message(content=response, role="assistant"))
                break


