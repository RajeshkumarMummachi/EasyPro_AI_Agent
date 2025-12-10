# EasyPro AI Agent

A simple and easy-to-use AI agent implementation using OpenAI's API. This agent can process user queries, maintain conversation context, and provide intelligent responses.

## Features

- 🤖 Interactive AI agent powered by OpenAI
- 💬 Maintains conversation history for context-aware responses
- ⚙️ Configurable settings (model, temperature, max tokens)
- 💾 Save and load conversation history
- 🎯 Simple and easy-to-use interface

## Prerequisites

- Python 3.7 or higher
- OpenAI API key

## Installation

1. Clone this repository:
```bash
git clone https://github.com/RajeshkumarMummachi/EasyPro_AI_Agent.git
cd EasyPro_AI_Agent
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Configuration

Edit `config.json` to customize the agent behavior:

```json
{
  "agent_name": "EasyPro AI Agent",
  "model": "gpt-3.5-turbo",
  "temperature": 0.7,
  "max_tokens": 500
}
```

- **agent_name**: Name of your AI agent
- **model**: OpenAI model to use (e.g., "gpt-3.5-turbo", "gpt-4")
- **temperature**: Controls randomness (0.0 to 1.0)
- **max_tokens**: Maximum length of response

## Usage

### Interactive Mode

Run the agent in interactive mode:

```bash
python main.py
```

### Available Commands

- Type your questions normally to interact with the agent
- `quit` or `exit` - Exit the program
- `clear` - Clear conversation history
- `history` - View conversation history
- `save` - Save conversation to a JSON file

### Using as a Library

```python
from ai_agent import AIAgent

# Initialize the agent
agent = AIAgent()

# Set system message (optional)
agent.add_system_message("You are a helpful assistant.")

# Process a query
response = agent.process_query("What is the capital of France?")
print(response)

# Clear history
agent.clear_history()

# Save conversation
agent.save_history("my_conversation.json")

# Load conversation
agent.load_history("my_conversation.json")
```

## Project Structure

```
EasyPro_AI_Agent/
├── ai_agent.py          # Core AI agent class
├── main.py              # Interactive CLI interface
├── config.json          # Configuration settings
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment file
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Example Interaction

```
==================================================
Welcome to EasyPro AI Agent!
==================================================

Type your queries below. Type 'quit' or 'exit' to stop.
Type 'clear' to clear conversation history.
Type 'history' to view conversation history.
Type 'save' to save conversation history.
--------------------------------------------------

You: What is artificial intelligence?

Agent: Artificial intelligence (AI) is the simulation of human 
intelligence processes by machines, especially computer systems. 
These processes include learning, reasoning, and self-correction.

You: Can you give me an example?

Agent: Sure! A common example is virtual assistants like Siri or 
Alexa that can understand voice commands and respond to questions.
```

## Requirements

See `requirements.txt` for the full list of dependencies:
- openai>=1.0.0
- python-dotenv>=1.0.0

## License

This project is open source and available for anyone to use and modify.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
