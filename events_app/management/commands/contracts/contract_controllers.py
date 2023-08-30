from .contract_views import create_contract
from .contract_models import save_contract

def controllers(choise):
    if choise == "1":
        contract = create_contract()
        save_contract(contract)
    elif choise == "2":
        print("Display contract")
    elif choise == "3":
        print("Update contract")
    elif choise == "4":
        print("Delete contract")

