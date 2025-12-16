import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

try:
    from agent import SimpleAgent
except ImportError:
    # Just in case they run it before installing deps or have path issues
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from agent import SimpleAgent

def main():
    print("--- Simple Python Agent (Gemini) ---")
    print("Type 'quit', 'exit', or 'bye' to stop.")
    
    try:
        agent = SimpleAgent()
    except ValueError as e:
        print(f"\nConfiguration Error: {e}")
        print("Please grab a free key from https://aistudio.google.com/ and set it as GOOGLE_API_KEY.")
        return

    print("\nAgent initialized! Say hello.")
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break
            
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break
            
        if not user_input:
            continue
            
        print("Agent: Thinking...", end="\r")
        response = agent.send_message(user_input)
        # Clear the "Thinking..." line and print response
        print(f"Agent: {response}")

if __name__ == "__main__":
    main()
