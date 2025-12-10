"""
Main script to run the EasyPro AI Agent
"""
from ai_agent import AIAgent


# Default system message for the agent
DEFAULT_SYSTEM_MESSAGE = "You are a helpful AI assistant. Be concise and friendly."


def main():
    """
    Main function to run the AI agent in interactive mode.
    """
    print("=" * 50)
    print("Welcome to EasyPro AI Agent!")
    print("=" * 50)
    print("\nType your queries below. Type 'quit' or 'exit' to stop.")
    print("Type 'clear' to clear conversation history.")
    print("Type 'history' to view conversation history.")
    print("Type 'save' to save conversation history.")
    print("-" * 50)
    
    try:
        # Initialize the agent
        agent = AIAgent()
        
        # Set a default system message
        agent.add_system_message(DEFAULT_SYSTEM_MESSAGE)
        
        # Interactive loop
        while True:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
            
            # Handle special commands
            if user_input.lower() in ['quit', 'exit']:
                print("\nThank you for using EasyPro AI Agent. Goodbye!")
                break
            
            elif user_input.lower() == 'clear':
                agent.clear_history()
                agent.add_system_message(DEFAULT_SYSTEM_MESSAGE)
                print("\nConversation history cleared.")
                continue
            
            elif user_input.lower() == 'history':
                print("\n--- Conversation History ---")
                for msg in agent.get_history():
                    role = msg['role'].capitalize()
                    content = msg['content']
                    print(f"{role}: {content}")
                print("--- End of History ---")
                continue
            
            elif user_input.lower() == 'save':
                filename = input("Enter filename (default: conversation.json): ").strip()
                if not filename:
                    filename = "conversation.json"
                agent.save_history(filename)
                print(f"\nConversation saved to {filename}")
                continue
            
            # Process the query
            response = agent.process_query(user_input)
            print(f"\nAgent: {response}")
    
    except ValueError as e:
        print(f"\nError: {e}")
        print("\nPlease make sure you have:")
        print("1. Created a .env file with your OPENAI_API_KEY")
        print("2. Set your OpenAI API key in the .env file")
        print("\nExample .env file:")
        print("OPENAI_API_KEY=your-api-key-here")
    
    except FileNotFoundError:
        print("\nError: config.json file not found.")
        print("Please ensure config.json exists in the current directory.")
    
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
