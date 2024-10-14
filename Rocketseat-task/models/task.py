"""
This module is responsible to define task model
"""


class Task:
    """Task model to be managed"""

    def __init__(
        self, title: str, description: str, user_id=int, completed=False
    ) -> None:
        self.title = title
        self.description = description
        self.completed = completed
        self.id = user_id

    def to_dict(self):
        """Method to return a dict for the current Task"""
        return {
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "id": self.id,
        }

    def toggle_completed(self):
        """Method to toggle task status (completed, not completed)"""
        self.completed = not self.completed
