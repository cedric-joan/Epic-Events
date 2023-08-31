from events_app.models import Event
from .event_views import create_event, menu
from .event_models import save_event

def controllers(choise):
    if choise == "1":
        event = create_event()
        save_event(event)
    elif choise == "2":
        event = get_event()
    elif choise == "3":
        print("Update event")
    elif choise == "4":
        print("Delete event")
    return menu()

# class ControllersEvent():

def get_event():
    events = Event.objects.all()
    for event in events:
        contract_id = event.contract_id
        client_id = event.client_id
        client_contact_id = client_contact_id,
        event_date_start = event_date_start,
        event_date_end = event_date_end,
        support_contact_id = support_contact_id,
        location = location,
        attendees = attendees,
        notes = notes,
    return print(f"{contract_id.id}\n{client_id.id}\n{client_contact_id}\n{event_date_start}\n{event_date_end}\n{support_contact_id}\n{location}\n{attendees}\n{notes}")