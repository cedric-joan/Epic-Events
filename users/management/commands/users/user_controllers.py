from .user_models import create_user, get_users, get_user_id, update_user, delete_user
from .user_views import input_create_user, display_users, display_delete_user, input_user_choise, input_update_user
from crm_project.utils import validate_name


def controllers(choise):
    if choise == "1":
        user = input_create_user()
        create_user(user)
        validate_name()
    elif choise == "2":
        users = get_users()
        display_users(users)
    elif choise == "3":
        users = get_users()
        display_users(users)
        user_id = input_user_choise()
        user = get_user_id(user_id)
        new_user = input_update_user(user)
        update_user(new_user, user_id)
    elif choise == "4":
        users = get_users()
        display_users(users)
        user_id = input_user_choise()
        user = get_user_id(user_id)
        delete_user(user_id)
        display_delete_user(user)
    return 


    