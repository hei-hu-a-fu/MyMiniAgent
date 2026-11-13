import abc

class tool(abc.ABC):
    @abc.abstractmethod
    def __init__(self, name, description):
        self.name = name
        self.description = description


    @abc.abstractmethod
    def run(self):
        """
        Execute the tool and return the result.
        """
        try:
            print(f"Running tool: {self.name}")
            tool_result = f"Tool {self.name} executed successfully."
            return tool_result
        except Exception as e:
            print(f"Error running tool: {e}")
            return f"Error running tool: {e}"