from datetime import datetime
import logging

debug_logger = logging.getLogger("debug_logger")
error_logger = logging.getLogger("error_logger")


class Task:
    _id_counter = 0

    def __init__(self, name, description):
        """
        Initializes a Task object with a unique ID, name, description, completion status (False), and creation date (current datetime).

        Args:
            name (str): The name of the task.
            description (str): The description of the task.

        Raises:
            ValueError: If the name or description is not provided.
        """

        if not name:
            logging.error("Le nom doit être fourni pour une tâche.")
            raise ValueError("Le nom doit être fourni pour une tâche.")
        if not description:
            logging.error("La description doit être fournie pour une tâche.")
            raise ValueError(
                "La description doit être fournie pour une tâche.")

        self.id = Task._id_counter
        Task._id_counter += 1
        self.name = name
        self.description = description
        self.completed = False
        self.created_date = datetime.now()
        debug_logger.debug(f"Création d'une nouvelle tâche : {name}")

    def mark_completed(self):
        """
        Marks the task as completed by setting the completion status to True.
        """
        self.completed = True
        debug_logger.debug(
            f"La tâche '{self.name}' a été marquée comme terminée.")

    def __str__(self):
        """
        Returns a string representation of the task, including its ID, name, description, completion status, and creation date.

        Returns:
            str: A formatted string representation of the task.
        """
        status = "Terminée" if self.completed else "Non terminée"
        return f"ID : {self.id}\nTâche : {self.name}\nDescription : {self.description}\nStatut : {status}\nDate de création : {self.created_date}\n"
