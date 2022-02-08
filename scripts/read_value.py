from brownie import accounts, SimpleStorage, config


def read_contract():
    # -1 index Always gets Latest deployed Contract Address
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retreive())


def main():
    read_contract()
