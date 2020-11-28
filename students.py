# Author: Fiona Nganga and Dirac Murairi
# this is the students file
from users_class import User


class Student(User):
    def __init__(self):
        self.borrower_name = 0
        self.book_liked = 0
        self.borrowed_books = {}
        self.books_in_possession = []
        self.penalty = 0
        super().__init__(self, name, id, email)
        print("=" * 50)
        print("Welcome to the ALU Library Management System!!!!\n"
              "What would you like to do today?\n"
              "If you are using our system for the first time please register as a new user\n"
              "If you are a registered user please choose the login option\n"
              "Press 1: To Borrow a book\n"
              "Press 2: To Extend borrowing time\n")
        print("=" * 50)

    def borrow_book(self, book_collection):
        print("The current books in the library are: ")
        for p in book_collection:
            print(p)
        borrower_name = input("Please enter your email address: ").lower()
        self.borrower_name = borrower_name
        book_liked = input("Please enter the book you'd like to borrow: ")
        self.book_liked = book_liked
        for v in book_collection:
            if v["name"] == book_liked:
                print("Book is available in the collection")
            else:
                print("Sorry that book is not in our collection, please try again from our collection")
        if len(self.books_in_possession) < 3 and self.penalty == 0:
            print("You can borrow a book")
            if self.book_liked not in self.borrowed_books.keys():
                self.borrowed_books.update({self.book_liked: borrower_name})
                print("The book is available,you can borrow it! ")
                print("You have the book for 2 weeks till you have to return it")
                self.books_in_possession.append(self.book_liked)
            else:
                print("Sorry, the book has been borrowed, try borrowing a different book")
