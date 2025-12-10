"""
Test suite for EasyPro AI Agent
"""

import pytest
from agent import AIAgent


class TestAIAgent:
    """Test cases for AIAgent class"""
    
    def test_agent_initialization(self):
        """Test that agent initializes correctly"""
        agent = AIAgent()
        assert agent.name == "EasyProAgent"
        assert agent.tasks == []
    
    def test_agent_custom_name(self):
        """Test agent initialization with custom name"""
        agent = AIAgent("CustomAgent")
        assert agent.name == "CustomAgent"
    
    def test_add_task(self):
        """Test adding a task"""
        agent = AIAgent()
        result = agent.add_task("Complete documentation")
        assert result is True
        assert len(agent.tasks) == 1
        assert "Complete documentation" in agent.tasks
    
    def test_add_invalid_task(self):
        """Test adding invalid tasks"""
        agent = AIAgent()
        # Test with None
        result = agent.add_task(None)
        assert result is False
        # Test with empty string
        result = agent.add_task("")
        assert result is False
        # Test with non-string
        result = agent.add_task(123)
        assert result is False
        assert len(agent.tasks) == 0
    
    def test_get_tasks(self):
        """Test retrieving tasks"""
        agent = AIAgent()
        agent.add_task("Task 1")
        agent.add_task("Task 2")
        tasks = agent.get_tasks()
        assert len(tasks) == 2
        assert "Task 1" in tasks
        assert "Task 2" in tasks
    
    def test_complete_task(self):
        """Test completing a task"""
        agent = AIAgent()
        agent.add_task("Task to complete")
        result = agent.complete_task("Task to complete")
        assert result is True
        assert len(agent.tasks) == 0
    
    def test_complete_nonexistent_task(self):
        """Test completing a task that doesn't exist"""
        agent = AIAgent()
        result = agent.complete_task("Nonexistent task")
        assert result is False
    
    def test_get_task_count(self):
        """Test getting task count"""
        agent = AIAgent()
        assert agent.get_task_count() == 0
        agent.add_task("Task 1")
        assert agent.get_task_count() == 1
        agent.add_task("Task 2")
        assert agent.get_task_count() == 2
        agent.complete_task("Task 1")
        assert agent.get_task_count() == 1
    
    def test_multiple_operations(self):
        """Test multiple operations in sequence"""
        agent = AIAgent("TestAgent")
        # Add multiple tasks
        agent.add_task("Write code")
        agent.add_task("Write tests")
        agent.add_task("Write documentation")
        assert agent.get_task_count() == 3
        
        # Complete one task
        agent.complete_task("Write tests")
        assert agent.get_task_count() == 2
        assert "Write tests" not in agent.get_tasks()
        assert "Write code" in agent.get_tasks()
        assert "Write documentation" in agent.get_tasks()
