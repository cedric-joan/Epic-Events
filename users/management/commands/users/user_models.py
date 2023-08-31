from users.models import User

def save_user(user):
    u = User(**user)
    u.save()

def delete_user(user):
    u = User(**user)
    u.delete()