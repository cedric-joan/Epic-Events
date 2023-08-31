from events_app.models import Contract, Event
from .contract_views import create_contract, menu
from .contract_models import save_contract

def controllers(choise):
    if choise == "1":
        contract = create_contract()
        save_contract(contract)
    elif choise == "2":
        contract = get_contract()
    elif choise == "3":
        print("Update contract")
    elif choise == "4":
        print("Delete contract")
    return menu()

# class ControllersContract():

def get_contract():
    contracts = Contract.objects.all()
    for contract in contracts:
        client_id = contract.client_id
        sales_contact_id = contract.sales_contact_id
        total_amount = contract.total_amount
        remaining_amount = contract.remaining_amount
    return print(f"{client_id.id}\n{sales_contact_id.id}\n{total_amount}\n{remaining_amount}")