from tasks.task import Task

import pytest


class TestCodeUnderTest:

    # create a task with a name and description
    def test_create_task_with_name_and_description(self):
        task = Task("Task 1", "Description 1")
        assert task.name == "Task 1"
        assert task.description == "Description 1"

    # mark a task as completed
    def test_mark_task_as_completed(self):
        task = Task("Task 1", "Description 1")
        assert task.completed is False
        task.mark_completed()
        assert task.completed is True

    # print a task's string representation
    def test_print_task_string_representation(self):
        task = Task("Task 1", "Description 1")
        id = task.id
        expected_output = "ID : " + str(id) + "\nTâche : Task 1\nDescription : Description 1\nStatut : Non terminée\nDate de création : " + str(task.created_date) + "\n"
        assert str(task) == expected_output

    # create multiple tasks and check if their IDs are unique
    def test_unique_task_ids(self):
        task1 = Task("Task 1", "Description 1")
        task2 = Task("Task 2", "Description 2")
        task3 = Task("Task 3", "Description 3")
        assert task1.id != task2.id
        assert task1.id != task3.id
        assert task2.id != task3.id

    # create a task with an empty name or description
    def test_create_task_with_empty_name_or_description(self):
        with pytest.raises(Exception):
            Task("", "Description 1")
        with pytest.raises(Exception):
            Task("Task 1", "")

    # mark a task as completed multiple times
    def test_mark_task_as_completed_multiple_times(self):
        task = Task("Task 1", "Description 1")
        assert task.completed is False
        task.mark_completed()
        assert task.completed is True
        task.mark_completed()
        assert task.completed is True
