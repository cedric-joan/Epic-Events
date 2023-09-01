from users.models import User



def create_user(user):
    u = User(**user)
    u.save()


def get_users():
    users = User.objects.all()
    return users

def get_user_id(user_id):
    user = User.objects.get(id=user_id)
    return user

def update_user(new_user, user_id):
    User.objects.filter(id=user_id).update(**new_user)


def delete_user(user_id):
    User.objects.filter(id=user_id).delete()