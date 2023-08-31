
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
            

def create_event():
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