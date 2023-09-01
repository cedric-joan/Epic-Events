from events_app.models import Client



def create_client(client):
    custumer = Client(**client)
    custumer.save()


def get_clients():
    clients = Client.objects.all()
    return clients

def get_client_id(client_id):
    client = Client.objects.get(id=client_id)
    return client

def update_client(new_client, client_id):
    Client.objects.filter(id=client_id).update(**new_client)

def delete_client(client_id):
    Client.objects.filter(id=client_id).delete()