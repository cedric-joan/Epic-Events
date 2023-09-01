from .contract_views import input_create_contract, display_contracts, display_delete_contract, input_contract_choise, input_update_contract
from .contract_models import create_contract, get_contracts, get_contract_id, update_contract, delete_contract
from crm_project.utils import validate_name


def controllers(choise):
    if choise == "1":
        contract = input_create_contract()
        create_contract(contract)
    elif choise == "2":
        contracts = get_contracts()
        display_contracts(contracts)
        validate_name()
    elif choise == "3":
        contract = get_contracts()
        display_contracts(contract)
        contract_id = input_contract_choise()
        contract = get_contract_id(contract_id)
        new_contract = input_update_contract(contract)
        update_contract(new_contract, contract_id)
    elif choise == "4":
        contracts = get_contracts()
        display_contracts(contracts)
        contract_id = input_contract_choise()
        contract = get_contract_id(contract_id)
        delete_contract(contract_id)
        display_delete_contract(contract)
    return 

