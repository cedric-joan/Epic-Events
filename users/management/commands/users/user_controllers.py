from users.models import User
from .user_models import save_user
from .user_views import create_user, menu

def controllers(choise):
    if choise == "1":
        user = create_user()
        save_user(user)
    elif choise == "2":
        user = get_user()
    elif choise == "3":
        print("Update user")
    elif choise == "4":
        print("Delete user")
    return menu()

def get_user():
    users = User.objects.all()
    for user in users:
        username = user.username
        email = user.email
        role = user.role
    return print(f"{username}\n{email}\n{role}")
    