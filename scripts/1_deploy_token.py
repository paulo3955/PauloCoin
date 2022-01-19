from brownie import PauloCoin
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000000000000, "ether")


def main():
    account = get_account()
    paulocoin = PauloCoin.deploy(initial_supply, {"from": account})
    print(paulocoin.name())