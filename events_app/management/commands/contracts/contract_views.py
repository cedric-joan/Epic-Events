
def menu():
    choise = ""
    while choise != "5":
        print(
            "\n1 - Create new contract\n2 - Display contract\n3 - Update contract\n4 - Delete contract\n5 - Quit"
        )

        choise = input()
        if not choise in ["1", "2", "3", "4", "5"]:
            print("*** Invalid choise ***\n")
        elif choise == "5":
            break
        else:
            return choise
            

def create_contract():
    client = int(input("client: "))
    sales_contact = int(input("sales_contact: "))
    total_amount = input("total_amount: ")
    remaining_amount = input("remaining_amount: ")
    
    contract = {
        "client_id": client,
        "sales_contact_id": sales_contact,
        "total_amount": total_amount,
        "remaining_amount": remaining_amount,
    }
    return contract