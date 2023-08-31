# from .client_controllers import ControllersClient

def menu():
    choise = ""
    while choise != "5":
        print(
            "\n1 - Create new client\n2 - Display client\n3 - Update client\n4 - Delete client\n5 - Quit"
        )

        choise = input()
        if not choise in ["1", "2", "3", "4", "5"]:
            print("Invalid choise !")
        elif choise == "5":
            break
        else:
            return choise
            

def create_client():
    first_name = input("first_name: ")
    last_name = input("last_name: ")
    email = input("email: ")
    phone_number = input("phone_number: ")
    compagny_name = input("compagny_name: ")
    sales_contact_id = int(input("sales_contact_id: "))
    client = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone_number": phone_number,
        "compagny_name": compagny_name,
        "sales_contact_id": sales_contact_id
    }
    return client

def display_client(clients):
    for client in clients:
        first_name = client.first_name
        last_name = client.last_name
        email = client.email
        phone_number = client.phone_number
        sales_contact_id = client.sales_contact_id
        print(f"{client.id}. {first_name} {last_name} {email} {phone_number} {sales_contact_id}")


def update_client_choise():
    return input("Entrez l'Id du client à modifier: ")

def update_client(client):
    first_name = input(f"current firt_name: {client.first_name} | new first_name (tapez entrer pour ignorer): ")
    last_name = input(f"current last_name: {client.last_name} | new last_name (tapez entrer pour ignorer): ")
    email = input(f"current email: {client.email} | new email (tapez entrer pour ignorer): ")
    phone_number = input(f"current phone_number: {client.phone_number} | new phone_number (tapez entrer pour ignorer): ")
    compagny_name = input(f"current compagny_name: {client.compagny_name} | new compagny_name (tapez entrer pour ignorer): ")
    sales_contact_id = input(f"current sales_contact: {client.sales_contact_id} | new sales_contact (tapez entrer pour ignorer): ")
    
    first_name = first_name if first_name else client.first_name
    last_name = last_name if last_name else client.last_name
    email = email if email else client.email
    phone_number = phone_number if phone_number else client.phone_number
    compagny_name = compagny_name if compagny_name else client.compagny_name
    sales_contact_id = int(sales_contact_id) if sales_contact_id else client.sales_contact_id

    client = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone_number": phone_number,
        "compagny_name": compagny_name,
        "sales_contact_id": sales_contact_id
    }
    return client


# current name: soro | new name (tapez entrer pour ignorer): 
# current name: soro | new name (tapez entrer pour ignorer): 
# current name: soro | new name (tapez entrer pour ignorer): 
# current name: soro | new name (tapez entrer pour ignorer): 
# current name: soro | new name (tapez entrer pour ignorer): 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 