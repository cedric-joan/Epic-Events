

def menu():
    choise = ""
    while choise != "5":
        print(
            "\n1 - Create new user\n2 - Display user\n3 - Update user\n4 - Delete client\n5 - Quit"
        )

        choise = input()
        if not choise in ["1", "2", "3", "4", "5"]:
            print("Invalid choise !")
        elif choise == "5":
            break
        else:
            return choise
        
def create_user():
    username = input("username: ")
    email = input("email: ")
    password = input("password: ")
    confirm_password = input("confirm_password: ")
    role = input("role [MGT, SAL, SUP]: ")
    user = {
        "username": username,
        "email": email,
        "password": password,
        "confirm_password": confirm_password,
        "role": role
    }
    return user