from events_app.models import Event


def save_event(event):
    c = Event(**event)
    c.save()

def delete_event(event):
    u = Event(**event)
    u.delete()