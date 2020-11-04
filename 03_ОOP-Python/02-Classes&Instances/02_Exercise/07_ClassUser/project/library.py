from typing import List, Dict, ClassVar, Tuple
from project.user import User


class Library:
    user_records: ClassVar[List[User]] = []
    books_available: ClassVar[Dict[str, list]] = {}
    rented_books: ClassVar[Dict[str, Dict[str, int]]] = {}
    rented_book_by_book_name: ClassVar[Dict[str, Tuple[str, int]]] = {}

    def add_user(self, user: User):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        self.user_records.append(user)

    def remove_user(self, user: User):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)
        # del self.rented_books[user.username]  # NOTE: THis maybe wrong

    def change_username(self, user_id: int, new_username: str):
        all_user_ids = [u.user_id for u in self.user_records]

        if user_id not in all_user_ids:
            return f"There is no user with id = {user_id}!"

        user_index = all_user_ids.index(user_id)
        if new_username == self.user_records[user_index].username:
            return "Please check again the provided username - it should be different than the username used so far!"

        self.user_records[user_index].username = new_username
        return f"Username successfully changed to: {new_username} for userid: {user_id}"
