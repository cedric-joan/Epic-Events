
def menu():
    while True:
        print(
            "1 - Create new event\n2 - Display event\n3 - Update event\n4 - Delete event"
        )

        choise = input()
        if not choise in ["1", "2", "3", "4"]:
            print("*** Invalid choise ***\n")
        else:
            return choise
            

def create_event():
    title = input("title: ")
    contract = int(input("contract: "))
    client = int(input("client: "))
    client_contact = int(input("client_contact: "))
    event_date_start = input("event_date_start: ")
    event_date_end = input("event_date_end: ")
    support_contact = int(input("support_contact: "))
    location = input("location: ")
    attendees = int(input("attendees: "))
    notes = input("notes: ")
    
    event = {
        "title": title,
        "contract_id": contract,
        "client": client,
        "client_contact": client_contact,
        "event_date_start": event_date_start,
        "event_date_end": event_date_end,
        "support_contact": support_contact,
        "location": location,
        "attendees": attendees,
        "notes": notes,
    }
    return event