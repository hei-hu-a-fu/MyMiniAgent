import memory
from src.agent import model

class agent:
    def __init__(self, name, description, env, tools , model):
        self.name = name
        self.description = description
        self.model = model.LLMModel
        self.tools = tools
        self.environment = env
        self.memory = memory.Memory(max_size=100, window_size=5)

    def agent_loop(self):
        while True:
            # Get the current context from memory
            current_context = self.memory.get_current_context(self.memory.Window_size)
            prompt = current_context
            response = self.model.generate_response(prompt)
            single_turn_tool_result = []
            if response.tools:
                for tool in response.tools:
                    single_turn_tool_result.append(tool.run())
                memory.add_message(memory.Message(content=single_turn_tool_result, role="tool"))
            else:
                memory.add_message(memory.Message(content=response, role="assistant"))
                break


