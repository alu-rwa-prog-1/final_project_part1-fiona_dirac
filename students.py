# Author: Fiona Nganga and Dirac Murairi
# this is the students file
from users_class import User
import datetime

day = datetime.datetime.now().strftime("%d")
month = datetime.datetime.now().month
day = int(day)
month = int(month)

class Student(User):
    def __init__(self, name, email, id, faculty, year):
        super().__init__(name, email, id)
        self.faculty = faculty
        self.year = year
        self.penalty = 0

    def update_date(self, student):
        """

        """

        if student["return_month"] in [1, 3, 5, 7, 8, 10, 12]:
            if student["return_day"] > 17:
                student["return_day"] = student["return_day"] + 14 - 31

                if student["return_month"] != 12:
                    student["return_month"] += 1
                else:
                    student["return_month"] = 1

            else:
                student["return_day"] += 14

        else:
            if student["return_day"] > 16:
                student["return_day"] = student["return_day"] + 14 - 30

                student["return_month"] += 1

            else:
                student["return_day"] += 14


    def extend_borrowing(self, borrowed_books):

        """

        """
        book_name = input("Please enter the book you'd like to borrow: ").upper()
        for student in borrowed_books:
            if student["name"] == self.name and book_name == student["book_name"]:
                if student["extended"] == 0:
                    self.update_date(student)
                    student["extended"] += 1
                    #message
                else:
                    print("Sorry, You have already extended your deadline")
                    print("You are expected to bring the book on {}/{}".format(student["return_day"], student["return_month"]))
            else:
                print("Sorry, You need to borrow that book in our library")

    def borrow_book(self, book_collection, borrowed_books):
        i = 0  # number of books in possession
        j = 0  # number of book the user can borrow
        #print all Books
        for book in book_collection:
            print("Book name: {} status: {}".format(book["name"], book["status"]))
        # check penalty
        if self.penalty == 0:
            for student in borrowed_books:
                if self.name == student["name"]:
                    i += 1
                    print("{} is already in possession of {} with ID: {}".format(self.name, student["book"],
                                                                                 student["id"]))
            if i > 2:
                print("Sorry, You already have 3 books into possession")
                return 0
            else:
                print("{} can borrow {} books or less".format(self.name, 3 - i))
        else:
            print("You have {} as penalty you need to pay before to take a book".format(self.penalty))
            return 0

        # check the number of book the user want to borrow
        z = int(0)  # check the number of tries someone make or the number of actions
        while True:
            j = int(input("How many book do you want to borrow: "))
            if 3 - i < j:
                if z == 1:
                    print("Sorry, You have entered an incorrect number twice")
                    return 0
                print("You can only borrow {} book(s) or less. Try again".format(3 - i))
                z += 1
            else:
                z = 0
                break

        # borrow book
        while z < j:
            i = 0
            book_name = input("Please enter the book you'd like to borrow: ").upper()
            for book in book_collection:
                if book["name"] == book_name:
                    if book["status"] == "NOT BORROWED":
                        print("=" * 50)
                        print("Book is available in the collection")
                        book["status"] = "BORROWED"
                        new = {"name": self.name, "mail": self.email,
                               "book_name": book_name, "month": month, "day": day,
                               "return_day" : day, "return_month": month, "extended": 0}
                        self.update_date(new)
                        borrowed_books.append(new)
                        i += 1
                        print("You have successfully borrowed this book")
                        print("=" * 50)
                    else:
                        print("{} ID: {} already borrowed".format(book_name, book["id"]))
            if i == 0:
                print("Sorry the book {} is not in our collection".format(book_name))

            z += 1


student1 = Student("Fiona", "f.nganga@alustudent.com", "2020", "CS", 2)
print(student1.name)

#borrowing book

lst_b = []
books = [{"name": "PYTHON", "id": "1", "status": "BORROWED", "author": "DIRAC"},
         {"name": "JAVA", "id": "2", "status": "NOT BORROWED", "author": "ACHILLE"},
         {"name": "PYTHON FOR EVERYBODY", "id": "3", "status": "NOT BORROWED", "author": "FIONA"},
         {"name": "C++", "id": "4", "status": "NOT BORROWED", "author": "FIONA"},
         {"name": "MFC", "id": "5", "status": "NOT BORROWED", "author": "ACHILLE"},
         {"name": "HARRY POTTER", "id": "6", "status": "BORROWED", "author": "DIRAC"},
         {"name": "PYTHON THE NORMAL WAY", "id": "7", "status": "BORROWED", "author": "DIRAC"}]
# student1.borrow_book(books, lst_b)
# print(lst_b)
# print(books)
# student1.extend_borrowing(lst_b)
# print(lst_b)
# student1.extend_borrowing(lst_b)
# print(lst_b)
