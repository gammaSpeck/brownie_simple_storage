from brownie import accounts, network, config, SimpleStorage


def get_account():
    return (
        accounts[0]
        if network.show_active() == "development"
        else accounts.add(config["wallets"]["from_key"])
    )


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    stored_value = simple_storage.retreive()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retreive()
    print(updated_stored_value)


def main():
    deploy_simple_storage()
