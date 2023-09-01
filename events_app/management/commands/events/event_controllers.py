from .event_views import input_create_event, display_delete_event, display_events, input_event_choise, input_update_event
from .event_models import create_event, get_event_id, get_events, update_event, delete_event
from crm_project.utils import validate_name



def controllers(choise):
    if choise == "1":
        event = input_create_event()
        create_event(event)
        validate_name()
    elif choise == "2":
        events = get_events()
        display_events(events)
    elif choise == "3":
        events = get_events()
        display_events(events)
        event_id = input_event_choise()
        event = get_event_id(event_id)
        new_event = input_update_event(event)
        update_event(new_event, event_id)
    elif choise == "4":
        events = get_events()
        display_events(events)
        event_id = input_event_choise()
        event = get_event_id(event_id)
        delete_event(event_id)
        display_delete_event(event)
    return