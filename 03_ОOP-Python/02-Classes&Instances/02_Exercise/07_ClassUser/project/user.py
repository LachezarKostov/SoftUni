class User:
    user_id: int
    username: str

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library: "Library"):

        for a, b in library.books_available.items():
            if a == author and book_name in b:
                self.books.append(book_name)
                if self.username not in library.rented_books:
                    library.rented_books[self.username] = {}

                library.books_available[author].remove(book_name)
                library.rented_books[self.username].update({book_name: days_to_return})
                library.rented_book_by_book_name[book_name] = (self.username, days_to_return)
            elif book_name in library.rented_book_by_book_name:
                days_to_return_from = library.rented_book_by_book_name[book_name][1]
                return f'The book "{book_name}" is already rented and will be available in ' + \
                       f"{days_to_return_from} days!"

    def return_book(self, author: str, book_name: str, library: "Library"):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"

        self.books.remove(book_name)
        library.books_available[author].append(book_name)
        del library.rented_books[self.username][book_name]

    def info(self):
        return ", ".join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.info()}"
