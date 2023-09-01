from .client_views import input_create_client, display_clients, input_client_choise, input_update_client
from .client_models import create_client, get_clients, get_client_id, update_client, delete_client
from crm_project.utils import validate_name



def controllers(choise):
    if choise == "1":
        client = input_create_client()
        create_client(client)
    elif choise == "2":
        clients = get_clients()
        display_clients(clients)
        validate_name()
    elif choise == "3":
        clients = get_clients()
        display_clients(clients)
        client_id = input_client_choise()
        client = get_client_id(client_id)
        new_client = input_update_client(client)
        update_client(new_client, client_id)
    elif choise == "4":
        clients = get_clients()
        display_clients(clients)
        client_id = input_client_choise()
        client = get_client_id(client_id)
        delete_client(client_id)
    return        