from typing import List
from project.task import Task


class Section:
    name: str
    tasks: List[Task]

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task.name in [t.name for t in self.tasks]:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):  # TODO check if task is completed b4 that
        list_of_tasks = [t.name for t in self.tasks]

        if task_name not in [t.name for t in self.tasks]:
            return f"Could not find task with the name {task_name}"

        self.tasks[list_of_tasks.index(task_name)].completed = True
        return f"Completed task {task_name}"

    def clean_section(self):

        b4_removal = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.completed]
        removed = b4_removal - len(self.tasks)

        return f"Cleared {removed} tasks."

    def view_section(self):
        return F"Section {self.name}:" + "\n" + \
               "\n".join([t.details() for t in self.tasks]) + "\n"
