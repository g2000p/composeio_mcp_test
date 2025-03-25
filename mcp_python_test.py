#!/usr/bin/env python3

class Task:
    """A class representing a task with a title, priority, and completion status."""
    
    def __init__(self, title: str, priority: int = 1):
        """
        Initialize a new task.
        
        Args:
            title (str): The title of the task
            priority (int, optional): Priority level (1-5). Defaults to 1.
        """
        self.title = title
        self.priority = max(1, min(5, priority))  # Ensure priority is between 1-5
        self.completed = False
        
    def complete(self):
        """Mark the task as completed."""
        self.completed = True
        
    def __str__(self):
        """Return a string representation of the task."""
        status = "✓" if self.completed else " "
        return f"[{status}] Priority {self.priority}: {self.title}"


class TaskManager:
    """A class to manage a collection of tasks."""
    
    def __init__(self):
        """Initialize an empty task manager."""
        self.tasks = []
        
    def add_task(self, title: str, priority: int = 1) -> Task:
        """
        Add a new task to the manager.
        
        Args:
            title (str): The title of the task
            priority (int, optional): Priority level (1-5). Defaults to 1.
            
        Returns:
            Task: The newly created task
            
        Raises:
            ValueError: If the title is empty
        """
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        
        task = Task(title, priority)
        self.tasks.append(task)
        return task
    
    def get_incomplete_tasks(self) -> list:
        """Return all incomplete tasks, sorted by priority."""
        return sorted(
            [task for task in self.tasks if not task.completed],
            key=lambda x: x.priority,
            reverse=True
        )
    
    def get_completed_tasks(self) -> list:
        """Return all completed tasks."""
        return [task for task in self.tasks if task.completed]
    
    def complete_task(self, title: str) -> bool:
        """
        Mark a task as completed by its title.
        
        Args:
            title (str): The title of the task to complete
            
        Returns:
            bool: True if task was found and completed, False otherwise
        """
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.complete()
                return True
        return False


def main():
    """Main function to demonstrate the task management system."""
    manager = TaskManager()
    
    try:
        # Add some sample tasks
        manager.add_task("Complete Python assignment", 5)
        manager.add_task("Read documentation", 3)
        manager.add_task("Take a break", 1)
        
        # Try to add an invalid task
        manager.add_task("")  # This will raise a ValueError
        
    except ValueError as e:
        print(f"Error: {e}")
    
    # Complete a task
    manager.complete_task("Read documentation")
    
    # Display all tasks
    print("\nIncomplete Tasks:")
    for task in manager.get_incomplete_tasks():
        print(task)
        
    print("\nCompleted Tasks:")
    for task in manager.get_completed_tasks():
        print(task)


if __name__ == "__main__":
    main()
