# Author: Fiona Nganga and Dirac Murairi
# This file has the main program flow
from students import Student
# from facilitators import Facilitator
from users_class import User


# from supervisors import Supervisor

def menu():
    print("=" * 50)
    print("Welcome to the ALU Library Management System!!!!\n"
          "What would you like to do today?\n"
          "If you are using our system for the first time please register as a new user\n"
          "If you are a registered user please choose the login option\n"
          "Press 1: To Login\n"
          "Press 2: To Register\n"
          "Press 3: To Log out\n ")
    print("=" * 50)


# we create the list of all the books we have in our library
books = [{"name": "PYTHON", "id": "1", "status": "BORROWED", "author": "DIRAC"},
         {"name": "JAVA", "id": "2", "status": "NOT BORROWED", "author": "ACHILLE"},
         {"name": "PYTHON FOR EVERYBODY", "id": "3", "status": "NOT BORROWED", "author": "FIONA"},
         {"name": "C++", "id": "4", "status": "NOT BORROWED", "author": "FIONA"},
         {"name": "MFC", "id": "5", "status": "NOT BORROWED", "author": "ACHILLE"},
         {"name": "HARRY POTTER", "id": "6", "status": "BORROWED", "author": "DIRAC"},
         {"name": "PYTHON THE NORMAL WAY", "id": "7", "status": "BORROWED", "author": "DIRAC"}]
# we create a list to hold borrowed books and their details
borrowed_books = list()

# we need to create a list for all the users in different categories and initialize with a few users
# this one belongs to the students
students_library = list()
student1 = {"name": "Fiona", "email_address": "f.nganga@alustudent.com", "nationality": "Kenyan", "password": "2020"}
student2 = {"name": "Dirac", "email_address": "d.murairi@alustudent.com", "nationality": "Congolese",
            "password": "2019"}
students_library.append(student1)
students_library.append(student2)
# for student in students_library:
#     print(student)

# this one belongs to the facilitators
facilitators_library = list()
facilitator1 = {"name": "Ella", "email_address": "e.karambizi@alustudent.com", "nationality": "Rwandan",
                "password": "2018"}
facilitator2 = {"name": "Mia", "email_address": "m.kila@alustudent.com", "nationality": "Tanzanian",
                "password": "2017"}
facilitators_library.append(facilitator1)
facilitators_library.append(facilitator2)
# for x in facilitators_library:
#     print(x)

# this one belongs to the supervisors
supervisors_library = list()
supervisor1 = {"name": "Terry", "email_address": "t.cruz@alustudent.com", "nationality": "Gambian",
               "password": "2016"}
supervisor2 = {"name": "Jax", "email_address": "j.jones@alustudent.com", "nationality": "South African",
               "password": "2015"}
supervisors_library.append(supervisor1)
supervisors_library.append(supervisor2)


# for y in supervisors_library:
#     print(y)

# we create register functions for different categories
# this is the function for registering a student
def register_student():
    name = input("What is your name? ")
    email_address = input("Please type in your ALU student email address: ").lower()
    nationality = input("Please type in your nationality: ")
    password = input("Please type in a password that you would like to use to sign in as a member in future: ")
    new_student = {"name": name, "email_address": email_address, "nationality": nationality, "password": password}
    students_library.append(new_student)
    print("You have successfully registered as a new user! You're welcome to use the library's resources!")


# this is the function for registering a facilitator
def register_facilitator():
    name = input("What is your name? ")
    email_address = input("Please type in your ALU staff email address: ").lower()
    nationality = input("Please type in your nationality: ")
    password = input("Please type in a password that you would like to use to sign in as a member in future: ")
    new_facilitator = {"name": name, "email_address": email_address, "nationality": nationality, "password": password}
    facilitators_library.append(new_facilitator)
    print("You have successfully registered as a new user! You're welcome to use the library's resources!")


# this is the function for registering a new supervisor
def register_supervisor():
    name = input("What is your name? ")
    email_address = input("Please type in your ALU issued email address: ").lower()
    nationality = input("Please type in your nationality: ")
    password = input("Please type in a password that you would like to use to sign in as a member in future: ")
    new_supervisor = {"name": name, "email_address": email_address, "nationality": nationality, "password": password}
    supervisors_library.append(new_supervisor)
    print("You have successfully registered as a new supervisor! You're welcome to administrator the "
          "library's resources!")


# method to display all books to users
# def display_books(book_collection):
#     print("All the available books are: ")
#     for b in book_collection:
#         print(b)
# alu_students = Student()
# alu_facilitators = Facilitator()

type = True
while type:
    menu()
    option = input("What would you like to do today? ").lower()
    if option == "1" or option == "one":
        print('Press 1: If you are a student\n'
              'Press 2: If you are a facilitator\n'
              'Press 3: If you are a supervisor')
        choice = input("What are you in the options above? Please type the number representing your category: ").lower()
        if choice == "1" or choice == "one":
            alu_students = Student()
            mail = input("Kindly input your email once again: ")
            for student in students_library:
                if student.get("email_address") == mail:
                    print("You are registered in our system!")
                    break
                else:
                    print("Sorry,you are not registered in our system, please try registering")
                    quit()
            print("What would you like to do today?\n"
                  "Press 1: To Borrow a book\n"
                  "Press 2: To extend the time you have borrowed for a certain book")
            pick = input("What would you like to do today? ")
            if pick == "1" or "one":
                alu_students.borrow_book(books, borrowed_books)
            elif pick == "2" or "two":
                alu_students.extend_borrowing(borrowed_books)
    if option == "2" or option == "two":
        print('Press 1: If you are registering as a student\n'
              'Press 2: If you are registering as a facilitator\n'
              'Press 3: If you are registering as a supervisor')
        option2 = input("What category are you under?Please enter the number here: ").lower()
        if option2 == "1" or option2 == "one":
            register_student()
        elif option2 == "2" or option2 == "two":
            register_facilitator()
        elif option2 == "3" or option2 == "three":
            register_supervisor()
    if option == "3" or "three":
        print("Thank you")
        break
    # elif option == "1" or option == "one":
    # elif option == "3" or option == "three":
