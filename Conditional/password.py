def lenght_password(password):
    cont = 0
    for i in password:
        cont += 1
    if(cont >= 8):
        return True
    else:
        return False


def has_number(password):
    for i in password:
        if i.isdigit():
            return True
    return False 


password = str(input("What is the password ?\n"))

try:

    if (lenght_password(password) and has_number(password)):
        print ("Strong")

    elif (lenght_password(password)):
        print("Moderate")

    else:
        print("Weak")

except:
    print("Invalid input. Please enter a valid password")