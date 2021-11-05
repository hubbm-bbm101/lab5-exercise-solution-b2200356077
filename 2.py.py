email = input("Write your e-mail: ")

def is_mail(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

if is_mail(email):
    print("Valid e-mail.")
else:
    print("Not valid e-mail.")