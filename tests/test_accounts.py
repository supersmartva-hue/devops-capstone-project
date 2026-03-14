import pytest
from service.models import accounts, create_account, list_accounts, read_account, update_account, delete_account

def test_create_account():
    accounts.clear()
    acc = {"id":1,"name":"Adeel"}
    create_account(acc)
    assert len(accounts) == 1
    assert accounts[0]["name"] == "Adeel"

def test_list_accounts():
    accounts.clear()
    create_account({"id":2,"name":"Test"})
    result = list_accounts()
    assert len(result) == 1

def test_read_account():
    accounts.clear()
    create_account({"id":3,"name":"ReadTest"})
    acc = read_account(3)
    assert acc["name"] == "ReadTest"

def test_update_account():
    accounts.clear()
    create_account({"id":4,"name":"OldName"})
    update_account(4, {"name":"NewName"})
    acc = read_account(4)
    assert acc["name"] == "NewName"

def test_delete_account():
    accounts.clear()
    create_account({"id":5,"name":"ToDelete"})
    delete_account(5)
    assert read_account(5) is None
