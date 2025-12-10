# EasyPro_AI_Agent

A simple AI Agent implementation with comprehensive test coverage.

## Features

- Basic AI Agent with task management capabilities
- Add, retrieve, and complete tasks
- Input validation for task operations
- 100% test coverage

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```python
from agent import AIAgent

# Create an agent
agent = AIAgent("MyAgent")

# Add tasks
agent.add_task("Complete documentation")
agent.add_task("Write tests")

# View tasks
print(agent.get_tasks())

# Complete a task
agent.complete_task("Write tests")

# Check remaining tasks
print(f"Tasks remaining: {agent.get_task_count()}")
```

## Testing

Run the test suite:

```bash
pytest test_agent.py -v
```

Run tests with coverage report:

```bash
pytest test_agent.py --cov=agent --cov-report=term-missing
```

## Test Results

- ✅ 9 test cases passing
- ✅ 100% code coverage
- ✅ All edge cases covered
