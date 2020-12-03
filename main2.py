# Author: Fiona Nganga and Dirac Murairi
# This file has the main program flow
from students import Student
from facilitators import Facilitator
from users_class import User
from supervisors import Supervisor



print("=" * 50)
user = int(input("""Welcome to the ALU Library Management System!!!!
"What would you like to do today?
"If you are using our system for the first time please register as a new user
"If you are a registered user please choose the login option
"Press 1: To Login
Press 2: To Register
{}""".format("=" * 50)))

if user == 1:
    login()
elif user == 2:
    register()
    login()
