
def menu():
    while True:
        print(
            "1 - Create new contract\n2 - Display contract\n3 - Update contract\n4 - Delete contract"
        )

        choise = input()
        if not choise in ["1", "2", "3", "4"]:
            print("*** Invalid choise ***\n")
        else:
            return choise
            

def create_contract():
    client = int(input("client: "))
    sales_contact = int(input("sales_contact: "))
    total_amount = input("total_amount: ")
    remaining_amount = input("remaining_amount: ")
    
    contract = {
        "client": client,
        "sales_contact": sales_contact,
        "total_amount": total_amount,
        "remaining_amount": remaining_amount,
    }
    return contract