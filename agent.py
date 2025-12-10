"""
EasyPro AI Agent - A simple AI agent implementation
"""


class AIAgent:
    """A basic AI Agent class"""
    
    def __init__(self, name="EasyProAgent"):
        """
        Initialize the AI Agent
        
        Args:
            name: The name of the agent
        """
        self.name = name
        self.tasks = []
    
    def add_task(self, task):
        """
        Add a task to the agent's task list
        
        Args:
            task: Task description string
        
        Returns:
            bool: True if task was added successfully
        """
        if task and isinstance(task, str):
            self.tasks.append(task)
            return True
        return False
    
    def get_tasks(self):
        """
        Get all tasks
        
        Returns:
            list: List of all tasks
        """
        return self.tasks
    
    def complete_task(self, task):
        """
        Remove a completed task
        
        Args:
            task: Task description to remove
        
        Returns:
            bool: True if task was removed successfully
        """
        if task in self.tasks:
            self.tasks.remove(task)
            return True
        return False
    
    def get_task_count(self):
        """
        Get the number of tasks
        
        Returns:
            int: Number of tasks
        """
        return len(self.tasks)
