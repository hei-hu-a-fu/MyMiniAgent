import abc

class Tool(abc.ABC):
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

class fakeTool(Tool):
    def __init__(self, name="Fake Tool", description="A fake tool for testing"):
        super().__init__(name, description)

    def run(self):
        """
        Execute the fake tool and return a fake result.
        """
        try:
            print(f"Running fake tool: {self.name}")
            # Simulate some processing
            fake_result = f"Fake result from {self.name}."
            return fake_result
        except Exception as e:
            print(f"Error running fake tool: {e}")
            return f"Error running fake tool: {e}"