from typing import List


class Task:
    name: str
    due_date: str
    comments = List
    completed = bool

    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str) -> str:
        if new_name == self.name:
            return "Name cannot be the same."

        self.name = new_name
        return new_name

    def change_due_date(self, new_date: str) -> str:  
        real_date = "".join([d for d in self.due_date if d.isdigit()])
        new_real_date = "".join([d for d in new_date if d.isdigit()])

        if real_date == new_real_date:
            return "Date cannot be the same."

        self.due_date = new_date
        return new_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if 0 <= comment_number < len(self.comments):
            self.comments[comment_number] = new_comment
            return ", ".join(self.comments)

        return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
