accounts = []

def create_account(account):
    accounts.append(account)
    return account

def list_accounts():
    return accounts

def read_account(account_id):
    for acc in accounts:
        if acc['id'] == account_id:
            return acc
    return None

def update_account(account_id, new_data):
    for i, acc in enumerate(accounts):
        if acc['id'] == account_id:
            accounts[i].update(new_data)
            return accounts[i]
    return None

def delete_account(account_id):
    global accounts
    accounts = [acc for acc in accounts if acc['id'] != account_id]
