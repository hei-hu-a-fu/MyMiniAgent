from openai import OpenAI
import os

class LLMModel:
    def __init__(self, model_name: str, baseurl: str):
        self.model_name = model_name
        # Initialize the model here (e.g., load weights, set up tokenizer, etc.)
        self.url = baseurl

    def generate_response(self, prompt: str, stream: bool = False) -> str:
        try:
            # Create an OpenAI client with the specified base URL
            client = OpenAI(base_url=self.url)
            # Generate a response using the model
            response = client.chat.completions.create(
                model=self.model_name,
                stream=stream,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message['content']
        except Exception as e:
            print(f"Error generating response: {e}")
            return f"Error generating response: {e}"