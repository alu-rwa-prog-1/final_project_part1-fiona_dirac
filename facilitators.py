# Author:  Fiona Nganga and Dirac Murairi
# this is the facilitators file

print("=" * 50)
print("Welcome to the ALU Library Management System!!!!\n"
      "What would you like to do today?\n"
      "If you are using our system for the first time please register as a new user\n"
      "If you are a registered user please choose the login option\n"
      "Press 1: To Borrow a book\n"
      "Press 2: To Return a book\n"
      "Press 3: To See available books\n ")
print("=" * 50)

class Facilitator(User):
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