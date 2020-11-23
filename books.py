# Author:
# this is a file for books in the library
# we create a list for all books and dictionaries with individual book details
books = list()
book1 = {"book name": "harry potter and the chamber of secrets", "book id": "1234567", "published date": "02/07/1998",
         "category": "digital", "status": "available", "acquisition date": "08/09/2020"}
book2 = {"book name": "learn python the hard way", "book id": "8765432", "published date": "09/19/2013",
         "category": "paper", "status": "available", "acquisition date": "01/11/2020"}


# this is the class that represents the books
class Books:
    def __init__(self):  # initialize needed variables as 0, the values assigned change later with user's input
        self.book_name = 0
        self.book_id = 0
        self.published_date = 0
        self.category = 0
        self.status = 0
        self.acquisition_date = 0
        self.delete_book = 0
        self.borrower_name = 0
        self.book_liked = 0
        self.borrowed_books = {}  # a dictionary that we create for borrowed books

    def add_books(self, book_collection):
        book_name = input("What is the title of the book you want to add?")
        book_id = input("What is the identification number of the book?")
        published_date = input("When was this book published? Please write in the dd/mm/yyyy format: ")
        category = input("What category does this book belong to? Is it digital or paper copy? ")
        status = input("What is the category of the book currently? Is it borrowed or available? ")
        acquisition_date = input("When did you acquire the book? Please write in the dd/mm/yyyy format: ")
        self.book_name = book_name
        self.book_id = book_id
        self.published_date = published_date
        self.category = category
        self.status = status
        self.acquisition_date = acquisition_date
        new_book = {"book name": book_name, "book id": book_id, "published date": published_date,
                    "category": category, "status": status, "acquisition date": acquisition_date}
        print("You have successfully added a new book to the library! ")
        book_collection.append(new_book)

    def remove_book(self, book_collection):
        print("The current books in the library are: ")
        for y in book_collection:
            print(y)
        delete_book = input("Please enter the identification number of the book you want to remove")
        self.delete_book = delete_book
        for c in book_collection:
            if c["book_id"] == delete_book:
                book_collection.remove(c)
                break

    def borrow_book(self, book_collection):
        print("The current books in the library are: ")
        for p in book_collection:
            print(p)
        borrower_name = input("Please enter your email address: ").lower()
        self.borrower_name = borrower_name
        book_liked = input("Please enter the identification number of the book you'd like to borrow: ")
        self.book_liked = book_liked
        if self.book_liked not in self.borrowed_books.keys():
            self.borrowed_books.update({book_liked: borrower_name})
            print("The book is available, have a good read! ")
        else:
            print("Sorry, the book has been borrowed, try borrowing a different book")

    def return_book(self, book_collection):
        return_book = input("Please enter the identification number of the book you would like to return: ")
        if return_book in self.borrowed_books:
            self.borrowed_books.pop(return_book)
            print("Thank you for returning the book!")
        else:
            print("Sorry, that book is not in our current collection")
