from web3 import Web3
from typing import Dict, List

web3 = Web3(Web3.HTTPProvider())


def create(entropy: str = None) -> Dict:
    return web3.eth.account.sign_transaction(entropy=entropy)


def private_key_to_account(private_key: str) -> Dict:
    return web3.eth.accounts.privateKeyToAccount(privateKey=private_key)


def sign_transaction(raw_tx: Dict, private_key: str) -> str:
    return web3.eth.account.sign_transaction(tx=raw_tx, privateKey=private_key)


def recover_transaction(raw_transaction: str) -> str:
    return web3.eth.accounts.recoverTransaction(rawTransaction=raw_transaction)


def hash_message(message: str) -> str:
    return web3.eth.accounts.hashMessage(message=message)


def sign(data: str, private_key: str) -> Dict:
    return web3.eth.accounts.sign(data=data, privateKey=private_key)


def recover():
    pass

def encrypt():
    pass

def decrypt():
    pass

def wallet():
    pass

def wallet_create():
    pass

def wallet_remove():
    pass

def wallet_clear():
    pass

def wallet_encrypt():
    pass

def wallet_decrypt():
    pass

def wallet_save():
    pass

def wallet_load():
    pass