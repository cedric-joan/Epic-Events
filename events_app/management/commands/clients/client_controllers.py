from .client_views import create_client
from .client_models import save_client

def controllers(choise):
    if choise == "1":
        client = create_client()
        save_client(client)
    elif choise == "2":
        print("Display client")
    elif choise == "3":
        print("Update client")
    elif choise == "4":
        print("Delete client")

