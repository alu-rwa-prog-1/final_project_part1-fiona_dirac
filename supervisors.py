# Author:  Fiona Nganga and Dirac Murairi
# this is the supervisors file


from users_class import User
from students import Student
from facilitators import Facilitator

class Supervisor(User):
    """docstring forSupervisor."""

    def __init__(self, name, id, email):
        super().__init__(name, id, email)

    def add_book(self, book_list):
        name = input("Enter the name of the book: ").upper()
        id = len(book_list) + 1
        author = input("Who is the author of the book: ").upper()
        new_book = {"name": name, "id": str(id), "status": "NOT BORROWED", "author": author}
        book_list.append(new_book)
        print("You have successfully added a book")

    def remove_book(self, book_list):
