from events_app.models import Event


def create_event(event):
    c = Event(**event)
    c.save()


def get_events():
    events = Event.objects.all()
    return events


def get_event_id(event_id):
    event = Event.objects.filter(id=event_id)
    return event

def update_event(new_event, event_id):
    Event.objects.filter(id=event_id).update(**new_event)


def delete_event(event_id):
    Event.objects.filter(id=event_id).delete()
    