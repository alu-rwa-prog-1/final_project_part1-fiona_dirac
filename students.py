# Author: Fiona Nganga and Dirac Murairi
# this is the students file
from users_class import User
import datetime

day = datetime.datetime.now().strftime("%d")
month = datetime.datetime.now().month

class Student(User):
    def __init__(self, name, mail, passworld, id, faculty, year):
        super().__init__(self, name, email, passworld)
        self.faculty = faculty
        self.id = id
        self.year = year
        self.penalty = 0

    def extend_borrowing(self, borrowed_books):

        """

        """
        book_name = input("Please enter the book you'd like to borrow: ").upper()
        for student in borrowed_books:
            if student["name"] == self.name and book_name == stuent["book_name"]:
                if student["extended"] == 0 :
                    if student["month"] in [1, 3, 5, 7, 8, 10, 12]:
                        if student["day"] > 17 and student["month"] != 7:
                            student["day"] = stuent["day"] + 14 - 31
                        elif student["day"] > 17 and student["month"] == 7:
                            student["day"] = stuent["day"] + 14 - 31
                        else:
                            student["day"] += 14

                        if student["month"] != 12:
                            student["month"] += 1
                        else:
                            student["month"] = 1
                else:
                    if student["day"] > 16:
                        student["day"] = stuent["day"] + 14 - 30
                    else:
                        student["day"] += 14
                    student["month"] += 1


    def borrow_book(self, book_collection, borrowed_books):
        i = 0              #number of books in possession
        j = 0              #number of book the user can borrow

        # check penalty
        if self.penalty == 0:
            for student in borrowed_books:
                if self.name == student["name"]:
                    i += 1
                    print("{} is already in possession of {} with ID: {}".format(self.name, student["book"], student["id"]))
            if i > 2:
                print("Sorry, You have more than 2 books")
                return 0
            else:
                print("You can only take {} books or less".format(3 - i))
        else:
            print("You have {} as penalty you need to pay before to take a book".format(self.penalty))

        # check the number of book the user want to borrow
        int z = 0  #check the number of tries someone make or the number of actions
        while True:
            j = int(input("How many book do you want to borrow: "))
            if 3 - i < j:
                if z == 1:
                    print("Sorry, You have entered an incorecte number twice")
                    return 0
                print("You can only borrow {} book(s) or less. Try again".format(3 - i))
                z += 1
            else:
                z = 0
                break

        #borrow book
        while (z < j):
            i = 0
            book_name = input("Please enter the book you'd like to borrow: ").upper()
            for book in book_collection:
                if book["name"] == book_name:
                    if book["status"] == "NOT BORROWED":
                        print("=" * 50)
                        print("Book is available in the collection")
                        book["status"] = "BORROWED"
                        new  = {"borrowed_name" : self.name, "mail" : self.mail,
                        "book_name": book_name, "month" : month, "Day" : day,
                        "extended" : 0}
                        borrowed_book.append(new)
                        i += 1
                        print("You have successfully borrowed this book")
                        print("=" * 50)
            if i == 0:
                print("Sorry the book {} is not in our collection".format(book_name))

            z += 1
