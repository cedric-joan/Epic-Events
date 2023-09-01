
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
            

def input_create_contract():
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

def display_contracts(contracts):
    for contract in contracts:
        client = contract.client
        sales_contact = contract.email
        total_amount = contract.total_amount
        remaining_amount = contract.remaining_amount
        print(f"{contract.id}. {client} {sales_contact} {total_amount} {remaining_amount}")

def input_contract_choise():
    return input("\nEnter contract ID: ")

def input_update_contract(contract):
    client = input(f"current client: {contract.client} | new client (tapez entrer pour ignorer): ")
    sales_contact = input(f"current sales_contact: {contract.sales_contact} | new sales_contact (tapez entrer pour ignorer): ")
    total_amount = input(f"current total_amount: {contract.total_amount} | new total_amount (tapez entrer pour ignorer): ")
    remaining_amount = input(f"current remaining_amount: {contract.remaining_amount} | new remaining_amount (tapez entrer pour ignorer): ")
    
    client = client if client else contract.client
    sales_contact = sales_contact if sales_contact else contract.sales_contact
    total_amount = total_amount if total_amount else contract.total_amount
    remaining_amount = remaining_amount if remaining_amount else contract.remaining_amount

    contract = {
        "client": client,
        "sales_contact": sales_contact,
        "total_amount": total_amount,
        "remaining_amount": remaining_amount
    }
    return contract

def display_delete_contract(contract):
    print(f"\nContrat :{contract.id} has deleted")