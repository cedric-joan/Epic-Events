
def menu():
    choise = ""
    while choise != "5":
        print(
            "\n1 - Create new event\n2 - Display event\n3 - Update event\n4 - Delete event\n5 - Quit"
        )

        choise = input()
        if not choise in ["1", "2", "3", "4", "5"]:
            print("*** Invalid choise ***\n")
        elif choise == "5":
            break
        else:
            return choise
            

def input_create_event():
    title = input("title: ")
    contract_id = int(input("contract_id: "))
    client_id = int(input("client_id: "))
    client_contact_id = int(input("client_contact_id: "))
    event_date_start = input("event_date_start: ")
    event_date_end = input("event_date_end: ")
    support_contact_id = int(input("support_contact_id: "))
    location = input("location: ")
    attendees = int(input("attendees: "))
    notes = input("notes: ")
    
    event = {
        "title": title,
        "contract_id": contract_id,
        "client_id": client_id,
        "client_contact_id": client_contact_id,
        "event_date_start": event_date_start,
        "event_date_end": event_date_end,
        "support_contact_id": support_contact_id,
        "location": location,
        "attendees": attendees,
        "notes": notes,
    }
    return event

def display_events(events):
    for event in events:
        title = event.title,
        contract_id = event.contract_id,
        client_id = event.client_id,
        client_contact_id = event.client_contact_id,
        event_date_start = event.event_date_start,
        event_date_end = event.event_date_end,
        support_contact_id = event.support_contact_id,
        location = event.location,
        attendees = event.attendees,
        notes = event.notes,
        print(f"{event.id}. {title} {contract_id} {client_id} {client_contact_id} {event_date_start} {event_date_end} {support_contact_id} {location} {attendees} {notes}")


def input_event_choise():
    return input("\nEnter event ID: ")


def input_update_event():
    title = input(f"current title: {event.title} | new title (tapez entrer pour ignorer): ")
    contract_id = int(input(f"current contract_id: {event.contract_id} | new contract_id (tapez entrer pour ignorer): "))
    client_id = int(input(f"current client_id: {event.client_id} | new client_id (tapez entrer pour ignorer): "))
    client_contact_id = int(input(f"current client_contact_id: {event.client_contact_id} | new client_contact_id (tapez entrer pour ignorer): "))
    event_date_start = input(f"current event_date_start: {event.event_date_start} | new event_date_start (tapez entrer pour ignorer): ")
    event_date_end = input(f"current event_date_end: {event.event_date_end} | new event_date_end (tapez entrer pour ignorer): ")
    support_contact_id = int(input(f"current support_contact_id: {event.support_contact_id} | new support_contact_id (tapez entrer pour ignorer): "))
    location = input(f"current location: {event.location} | new location (tapez entrer pour ignorer): ")
    attendees = int(input(f"current attendees: {event.attendees} | new attendees (tapez entrer pour ignorer): "))
    notes = input(f"current notes: {event.notes} | new notes (tapez entrer pour ignorer): ")
    
    title = title if title else event.title
    contract_id = contract_id if contract_id else event.contract_id
    client_id = client_id if client_id else event.client_id
    client_contact_id = client_contact_id if client_contact_id else event.client_contact_id
    event_date_start = event_date_start if event_date_start else event.event_date_start
    event_date_end = event_date_end if event_date_end else event.event_date_end
    support_contact_id = support_contact_id if support_contact_id else event.support_contact_id
    location = location if location else event.location
    attendees = attendees if attendees else event.attendees
    notes = notes if notes else event.notes

    event = {
        "title": title,
        "contract_id": contract_id,
        "client_id": client_id,
        "client_contact_id": client_contact_id,
        "event_date_start": event_date_start,
        "event_date_end": event_date_end,
        "support_contact_id": support_contact_id,
        "location": location,
        "attendees": attendees,
        "notes": notes,
    }
    return event

def display_delete_event(event):
    print(f"\nL'événement {event.id} has deleted")