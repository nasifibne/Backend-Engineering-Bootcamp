print("=======REGISTRATION VALIDATOR=======")
username = input("enter your username: ")
age =int(input("enter your age: "))
email = input ("enter your email id: ")
password = input("enter your password: ")

if username and age>=13 and email and len(password) >=8:
    terms = input("Do you accept all the terms and condition? ")
    if terms:
        print("Registration Succeeds.")
    else:
        print("Registration failed.")
else:
    print("Registration failed.")
