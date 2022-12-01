from web3 import Web3
from methods.get_contract_abi import get_contract_abi
from keys import HTTP_PROVIDER
from chain_info import chain_details


def approve(token_address, spender_address, amount, proxy_contract=None):
    w3 = Web3(Web3.HTTPProvider(HTTP_PROVIDER))
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

    print(w3.toHex(w3.keccak(signed_txn.rawTransaction)))

def main():
    token_address = Web3.toChecksumAddress('0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8')
    spender_address = Web3.toChecksumAddress('0xE592427A0AEce92De3Edee1F18E0157C05861564')
    proxy_contract = Web3.toChecksumAddress('0x8b194bEae1d3e0788A1a35173978001ACDFba668')
    amount = 0 * (10 ** 18)
    approve(token_address, spender_address, amount, proxy_contract)


if __name__ == "__main__":
    main()



