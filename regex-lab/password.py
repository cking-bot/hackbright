import re 
def is_strong():

    print("Enter a password")
    password = input()

    password_validation = re.compile(r"(?=.[A-Za-z]{8,}[0-9]$).*")

    if not password_validation.match(password):
        print("Is not a strong password")
    else: 
        print("Is a strong password")

is_strong()



    