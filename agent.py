import google.generativeai as genai
import os
from tools import calculate, get_current_time, get_system_info, generate_random_number, get_current_weather

class SimpleAgent:
    def __init__(self):
        """
        Initializes the agent with the API key and tools.
        """
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it in a .env file or your shell.")
            
        genai.configure(api_key=api_key)
        
        # Tools map for the agent to know how to call them
        self.tools = [calculate, get_current_time, get_system_info, generate_random_number, get_current_weather]
        
        # Initialize the model with tools
        self.model = genai.GenerativeModel(
            model_name='gemini-flash-latest', # standard alias for the latest flash model
            tools=self.tools
        )
        
        # Start a chat session with automatic function calling enabled
        self.chat = self.model.start_chat(enable_automatic_function_calling=True)

    def send_message(self, user_message: str) -> str:
        """
        Sends a message to the agent and gets a response.
        Handles tool calls automatically via the SDK.
        """
        try:
            response = self.chat.send_message(user_message)
            return response.text
        except Exception as e:
            return f"An error occurred: {e}"
