from .event_views import create_event
from .event_models import save_event

def controllers(choise):
    if choise == "1":
        event = create_event()
        save_event(event)
    elif choise == "2":
        print("Display event")
    elif choise == "3":
        print("Update event")
    elif choise == "4":
        print("Delete event")

