



def menu():
    choise = ""
    while choise != "5":
        print(
            "\n1 - Create new user\n2 - Display user\n3 - Update user\n4 - Delete client\n5 - Quit"
        )

        choise = input()
        if not choise in ["1", "2", "3", "4", "5"]:
            print("*** Invalid choise ***\n")
        elif choise == "5":
            break
        else:
            return choise
        
def input_create_user():
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

def display_users(users):
    for user in users:
        username = user.username
        email = user.email
        role = user.role
        print(f"{user.id}. {username} {email} {role}")

def input_user_choise():
    return input("\nEnter user ID: ")

def input_update_user(user):
    username = input(f"current username: {user.username} | new username (tapez entrer pour ignorer): ")
    email = input(f"current email: {user.email} | new email (tapez entrer pour ignorer): ")
    role = input(f"current role: {user.role} | new role (tapez entrer pour ignorer): ")
    
    username = username if username else user.username
    email = email if email else user.email
    role = role if role else user.role

    user = {
        "username": username,
        "email": email,
        "role": role
    }
    return user

def display_delete_user(user):
    print(f"\nL'utilisateur {user.username} has deleted")