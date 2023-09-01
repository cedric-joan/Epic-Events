from events_app.models import Contract




def create_contract(contract):
    contract_save = Contract(**contract)
    contract_save.save()


def get_contracts():
    contracts = Contract.objects.all()
    return contracts

def get_contract_id(contract_id):
    contract = Contract.objects.get(id=contract_id)
    return contract

def update_contract(new_contract, contract_id):
    Contract.objects.filter(id=contract_id).update(**new_contract)

def delete_contract(contract_id):
    Contract.objects.filter(id=contract_id).delete()