import re
import requests

def validate_email(email_address, password, indice):
    #check with re module if email is correct
    if re.match(r"[^@]+@[^@]+\.[^@]+", email_address):
        response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params = {'email': email_address})

        status = response.json()['status']
        if status == "valid":
            #open files
            #check password
            return 1
        else:
            return 0

def connect(numb):
    if numb == 1:
        #create_student and dis menu
        return 1
    elif numb == 2:
        #create facilitator and dis menu
        return 1
    elif numb == 3:
        #create su and dis menu
        return 1

def login():
    email_address = input("Enter your email address: ").lower()
    password = input("Enter your password: ")
    email = email_address.split("@")
    if email[1] != 'alustudent.com' and email[1] != 'alueducation.com':
        print("Your email address is not reconnised as a ALU mail")
        print("please use your ALU mail address")
        return 0

    return_value = validate_email(email, password, 1)
    if return_value == 1 and email[1] == 'alustudent.com':
        connect(1)
        return 1
    elif return_value == 2 and email[1] != 'alueducation.com':
        connect(2)
        return 1
    elif return_value == 3:
        connect(3)
        return 1
    else:
        print("Email address not found")
        return 0

def register_user():
    name = input("What is your name? ")
    email_address = input("Please type in your ALU issued email address: ").lower()
    email = email_address.split("@")
    if email[1] != 'alustudent.com' and email[1] != 'alueducation.com':
        print("Your email address is not reconnised as a ALU mail")
        print("please use your ALU mail address")
        return 0
    return_value = validate_email(email, password, 2)
    if return_value != 1:
        print("Sorry, your Email address could not be found")
        return 0
    nationality = input("Please type in your nationality: ")
    password = input("Please type in a password: ")
    print("""You have successfully registered as a new supervisor!
    You're welcome to administrator the library's resources!""")
    return 1

def user_menu():
    #dis menu
    return 1

def supervisor_menu():
    #dis menu
    return 1

# print(validate_email("d.murair@alustudent.com", "dirac"))
