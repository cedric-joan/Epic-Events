from events_app.models import Contract


def save_contract(contract):
    contract_save = Contract(**contract)
    contract_save.save()

def delete_contract(contract):
    contract_delete = Contract(**contract)
    contract_delete.delete()