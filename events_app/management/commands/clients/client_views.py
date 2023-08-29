
def menu():
    while True:
        print(
            "1 - Create new client\n2 - Display client\n3 - Update client\n4 - Delete client"
        )

        choise = input()
        if not choise in ["1", "2", "3", "4"]:
            print("Invalid choise !")
        else:
            return choise
            

def create_client():
    first_name = input("first_ name: ")
    last_name = input("last_name: ")
    email = input("email: ")
    phone_number = input("phone_number: ")
    compagny_name = input("compagny_name: ")
    sales_contact = int(input("sales_contact: "))
    client = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone_number": phone_number,
        "compagny_name": compagny_name,
        "sales_contact_id": sales_contact
    }
    return client