from web3 import Web3
from methods.get_contract_abi import get_contract_abi
from providers import get_http_provider
from chain_info import chain_details
from typing import Optional, Dict, Any, List


class Web3Manager:
    w3 = Web3(Web3.HTTPProvider(HTTP_PROVIDER))

    def __init__(self, chain, account_address, private_key):
        """
        :param chain:
        :param private_key:
        """
        self.chain = chain
        self.account_address = account_address
        self.private_key = private_key
        self.w3 = Web3(Web3.HTTPProvider(chain))



    def approve(self, token_address, spender_address, amount=(2**256 - 1), proxy_contract=None):
        """
        :param token_address: Token contract address that we want to allow spending
        :param spender_address: Address that will spend our tokens
        :param amount: Allowance amount, maximum if not provided
        :param proxy_contract: In case token address is a proxy contract, and approve function is in proxy contract
        :return: Approve transaction hash
        """

        if proxy_contract:
            abi = get_contract_abi(proxy_contract)
        else:
            abi = get_contract_abi(token_address)
        token_contract = self.w3.eth.contract(address=token_address, abi=abi)
        approve_tx = token_contract.functions.approve(spender_address, amount).build_transaction({
            'chainId': chain_details['chainId'],
            'gas': chain_details['gas'],
            'maxFeePerGas': chain_details['maxFeePerGas'],
            'maxPriorityFeePerGas': chain_details['maxPriorityFeePerGas'],
            'nonce': self.w3.eth.get_transaction_count(my_address),
        })
        signed_txn = self.w3.eth.account.sign_transaction(approve_tx, private_key=my_private_key)
        self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)

        return self.w3.toHex(self.w3.keccak(signed_txn.rawTransaction))

