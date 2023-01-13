from web3 import Web3
from methods.get_contract_abi import get_contract_abi
from providers import HTTP_PROVIDER
from chain_info import chain_details


class Web3Manager:

    w3 = Web3(Web3.HTTPProvider(HTTP_PROVIDER))

    def __init__(self, chain, private_key):
        """
        :param chain:
        :param private_key:
        """
        self.chain = chain
        self.private_key = private_key


    def approve(self, my_address, token_address, spender_address, amount=(2**256 - 1), proxy_contract=None):
        """
        :param my_address: Account that will add approve to other
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
        token_contract = w3.eth.contract(address=token_address, abi=abi)
        approve_tx = token_contract.functions.approve(spender_address, amount).build_transaction({
            'chainId': chain_details['chainId'],
            'gas': chain_details['gas'],
            'maxFeePerGas': chain_details['maxFeePerGas'],
            'maxPriorityFeePerGas': chain_details['maxPriorityFeePerGas'],
            'nonce': w3.eth.get_transaction_count(my_address),
        })
        signed_txn = w3.eth.account.sign_transaction(approve_tx, private_key=my_private_key)
        w3.eth.send_raw_transaction(signed_txn.rawTransaction)

        return w3.toHex(w3.keccak(signed_txn.rawTransaction))
