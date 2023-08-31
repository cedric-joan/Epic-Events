from events_app.models import Client
from .client_views import create_client, menu, display_client, update_client_choise, update_client
from .client_models import save_client, get_client, get_client_id, update_client_m
from crm_project.utils import validate_name

def controllers(choise):
    if choise == "1":
        client = create_client()
        save_client(client)
    elif choise == "2":
        clients = get_client()
        display_client(clients)
        validate_name()
    elif choise == "3":
        clients = get_client()
        display_client(clients)
        client_id = update_client_choise()
        client = get_client_id(client_id)
        new_client = update_client(client)
        update_client_m(new_client, client_id)
    elif choise == "4":
        print("Delete client")
    return 
            

# class ControllersClient():


        