class agent:
    def __init__(self, name, description, env):
        self.name = name
        self.description = description
        self.tools = []
        self.environment = env
        self.memory = []

    def greet(self):
        return f"Hello, my name is {self.name}."