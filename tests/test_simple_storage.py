from brownie import accounts, SimpleStorage


def test_deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retreive()
    assert starting_value == 0


def test_updating_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    expected = 15
    transaction = simple_storage.store(expected, {"from": account})
    transaction.wait(1)
    assert expected == simple_storage.retreive()
