from events_app.models import Client

def save_client(client):
    c = Client(**client)
    c.save()