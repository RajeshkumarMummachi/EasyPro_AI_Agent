"""
EasyPro AI Agent - A simple AI agent implementation using OpenAI API
"""
import os
import json
from typing import List, Dict, Optional
from openai import OpenAI
from dotenv import load_dotenv


class AIAgent:
    """
    A simple AI agent that can process user queries and maintain conversation context.
    """
    
    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the AI Agent with configuration.
        
        Args:
            config_path: Path to the configuration file
        """
        # Load environment variables
        load_dotenv()
        
        # Load configuration
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        # Initialize OpenAI client
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        self.client = OpenAI(api_key=api_key)
        
        # Initialize conversation history
        self.conversation_history: List[Dict[str, str]] = []
        
        # Agent properties from config
        self.agent_name = self.config.get("agent_name", "AI Agent")
        self.model = self.config.get("model", "gpt-3.5-turbo")
        self.temperature = self.config.get("temperature", 0.7)
        self.max_tokens = self.config.get("max_tokens", 500)
        
    def add_system_message(self, message: str):
        """
        Add a system message to set the agent's behavior.
        
        Args:
            message: The system message content
        """
        self.conversation_history.append({
            "role": "system",
            "content": message
        })
    
    def process_query(self, user_input: str) -> str:
        """
        Process a user query and return the agent's response.
        
        Args:
            user_input: The user's input message
            
        Returns:
            The agent's response
        """
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            # Extract assistant's response
            assistant_message = response.choices[0].message.content
            
            # Add assistant's response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            error_msg = f"Error processing query: {str(e)}"
            print(error_msg)
            return error_msg
    
    def clear_history(self):
        """Clear the conversation history."""
        self.conversation_history = []
    
    def get_history(self) -> List[Dict[str, str]]:
        """
        Get the current conversation history.
        
        Returns:
            List of conversation messages
        """
        return self.conversation_history
    
    def save_history(self, filepath: str):
        """
        Save conversation history to a file.
        
        Args:
            filepath: Path to save the history
        """
        with open(filepath, 'w') as f:
            json.dump(self.conversation_history, f, indent=2)
    
    def load_history(self, filepath: str):
        """
        Load conversation history from a file.
        
        Args:
            filepath: Path to load the history from
        """
        with open(filepath, 'r') as f:
            self.conversation_history = json.load(f)
