# Author:  Fiona Nganga and Dirac Murairi
# this is the facilitators file

from users_class import User
import datetime
import calendar

day = datetime.datetime.now().strftime("%d")
month = datetime.datetime.now().month
day = int(day)
month = int(month)


# this is a class for facilitators

class Facilitator(User):
    """
           Facilitator
           ---------
           The facilitator is a user of the library.
           The facilitator can:
               -   Borrow a book
               -   Extend Borrowing time for a book
           """

    def __init__(self, name, email, id, faculty, year):
        super().__init__(name, email, id)
        self.faculty = faculty
        self.year = year
        self.penalty = 0

    def update_date(self, student):
        """
        update_date
        -----------
        This method update the date accordingly to the number of days in a month.
        it recieves as arguments a dictionary.
        update_date(dictionary)
        ;return:nothing
        """
        # The naming will be fixed in the next submission. we keep student for the moment.
        # for months those have 31 days
        if student["return_month"] in [1, 3, 5, 7, 8, 10, 12]:
            if student["return_day"] > 17:
                student["return_day"] = student["return_day"] + 14 - 31

                if student["return_month"] != 12:
                    student["return_month"] += 1
                else:
                    student["return_month"] = 1

            else:
                student["return_day"] += 14

        # for months those have 30 days and february
        else:
            if student["return_month"] != 2:
                if student["return_day"] > 16:
                    student["return_day"] = student["return_day"] + 14 - 30

                    student["return_month"] += 1
                else:
                    student["return_day"] += 14
            else:
                # 366 days in a year where fabruary has 29 days
                if calendar.isleap(year):
                    if student["return_day"] > 15:
                        student["return_day"] = student["return_day"] + 14 - 29

                        student["return_month"] += 1
                    else:
                        student["return_day"] += 14
                # 365 days in a year where fabruary has 28 days
                else:
                    if student["return_day"] > 14:
                        student["return_day"] = student["return_day"] + 14 - 28

                        student["return_month"] += 1
                    else:
                        student["return_day"] += 14

    def extend_borrowing(self, borrowed_books):

        """
        extend_borrowing
        ----------------
        This method allows the user to extend to 14 days the time he had borrowed a book.
        it receives as argument a list of dictionaries holding information about book_borrowed.
        extend_borrowing(borrowed_books)
        ;return: nothing
        """
        book_name = input("Please enter the book you'd like to borrow: ").upper()
        for facilitator in borrowed_books:
            if facilitator["name"] == self.name and book_name == facilitator["book_name"]:
                if facilitator["extended"] < 2:
                    self.update_date(facilitator)
                    facilitator["extended"] += 1
                    print("You have successfully extended your deadline")
                else:
                    print("Sorry, You have already extended your deadline")
                    print("You are expected to bring the book on {}/{}".format(facilitator["return_day"],
                                                                               facilitator["return_month"]))
            else:
                print("Sorry, You need to borrow that book in our library")

    def borrow_book(self, book_collection, borrowed_books):

        """
        borrowed_books
        --------------
        This method allows a student to borrow a certain number of books
        less than 3 from the library.
        It adds the books borrowed to the list of books in people’s possession.
        it recieves as argument a list of dictionaries holding informations about book_collection.
        it recieves as argument a list of dictionaries holding informations about book_borrowed.
        borrow_book(book_collection, borrowed_books)
        ;return: 0 when there is an error.
        """

        i = 0  # number of books in possession
        j = 0  # number of book the user can borrow

        # print all Books
        for book in book_collection:
            print("Book name: {} status: {}".format(book["name"], book["status"]))
        # check penalty
        if self.penalty == 0:
            for facilitator in borrowed_books:
                if self.name == facilitator["name"]:
                    i += 1
                    print("{} is already in possession of {} with ID: {}".format(self.name, facilitator["book"],
                                                                                 facilitator["book_id"]))
            if i > 4:
                print("Sorry, You already have 5 books into possession")
                return 0
            else:
                print("You can only take {} books or less".format(5 - i))
        else:
            print("You have {} as penalty you need to pay before to take a book".format(self.penalty))

        # check the number of book the user want to borrow
        z = int(0)  # check the number of tries someone make or the number of actions
        while True:
            j = int(input("How many book do you want to borrow: "))
            if 5 - i < j:
                if z == 1:
                    print("Sorry, You have entered an incorrect number twice")
                    return 0
                print("You can only borrow {} book(s) or less. Try again".format(5 - i))
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
                               "book_name": book_name, "book_id": book["id"], "month": month, "Day": day,
                               "return_day": day, "return_month": month, "extended": 0}
                        self.update_date(new)
                        borrowed_books.append(new)
                        i += 1
                        book["status"] = "BORROWED"
                        print("You have successfully borrowed this book")
                        print("=" * 50)
            if i == 0:
                print("Sorry the book {} is not in our collection".format(book_name))

            z += 1


# student1 = Facilitator()
# print(student1.name)

# borrowing book

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
# student1.extend_borrowing(lst_b)
# print(lst_b)
