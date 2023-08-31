from events_app.models import Client


def save_client(client):
    c = Client(**client)
    c.save()

def delete_client(client):
    c = Client(**client)
    c.delete()

def get_client():
    clients = Client.objects.all()
    return clients

def get_client_id(client_id):
    client = Client.objects.get(id=client_id)
    return client

def update_client_m(new_client, client_id):
    Client.objects.filter(id=client_id).update(**new_client)