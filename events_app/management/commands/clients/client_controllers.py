from .client_views import create_client
from .client_models import save_client

def controllers(choise):
    if choise == "1":
        client = create_client()
        save_client(client)
    elif choise == "2":
        print("display client")
    else:
        print("invalid choise")

