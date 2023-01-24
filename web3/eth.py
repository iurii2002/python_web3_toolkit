from providers import get_http_provider
from web3 import Web3
from typing import Dict, List

web3 = Web3(Web3.HTTPProvider(get_http_provider('ETH_MAINNET')))

# Properties


def eth_default_account():
    return web3.eth.default_account


def eth_default_block():
    return web3.eth.default_block


def eth_syncing():
    return web3.eth.syncing


def eth_coinbase():
    return web3.eth.coinbase


def eth_mining():
    return web3.eth.mining


def eth_hashrate():
    return web3.eth.hashrate


def eth_max_priority_fee():
    return web3.eth.max_priority_fee


def eth_gas_price():
    return web3.eth.gas_price


def eth_accounts():
    return web3.eth.accounts


def eth_block_number():
    return web3.eth.block_number


def eth_protocol_version():
    return web3.eth.protocol_version


def eth_chain_id():
    return web3.eth.chain_id


# METHODS

def eth_get_balance(account, block=None):
    if block and block > eth_get_block_number():
        raise ValueError("Block number should less than latest")
    return web3.eth.get_balance(account=web3.toChecksumAddress(account), block_identifier=block)


def eth_get_block_number():
    return web3.eth.get_block_number()


def eth_get_storage_at(account, position, block=None):
    if block and block > eth_get_block_number():
        raise ValueError("Block number should less than latest")
    return web3.eth.get_storage_at(account=web3.toChecksumAddress(account), positions=position, block_identifier=block)


def eth_get_proof(account, position, block=None):
    if block and block > eth_get_block_number():
        raise ValueError("Block number should less than latest")
    return web3.eth.get_proof(account=web3.toChecksumAddress(account), positions=position, block_identifier=block)


def eth_get_code(account, block=None):
    if block and block > eth_get_block_number():
        raise ValueError("Block number should less than latest")
    return web3.eth.get_code(account=web3.toChecksumAddress(account), block_identifier=block)


def eth_get_block(block=None, full_transactions=False):
    if block and block > eth_get_block_number():
        raise ValueError("Block number should less than latest")
    return web3.eth.get_block(block_identifier=block, full_transactions=full_transactions)


def eth_get_block_transaction_count(block=None):
    if block and block > eth_get_block_number():
        raise ValueError("Block number should less than latest")
    return web3.eth.get_block_transaction_count(block_identifier=block)


def eth_get_uncle_by_block(block=None, uncle_index=0):
    if block and block > eth_get_block_number():
        raise ValueError("Block number should less than latest")
    return web3.eth.get_uncle_by_block(block_identifier=block, uncle_index=uncle_index)


def eth_get_uncle_count(block=None):
    if block and block > eth_get_block_number():
        raise ValueError("Block number should less than latest")
    return web3.eth.get_uncle_count(block_identifier=block)


def eth_get_transaction(tx):
    return web3.eth.get_transaction(transaction_hash=tx)


def eth_get_raw_transaction(tx):
    return web3.eth.get_raw_transaction(transaction_hash=tx)


def eth_get_transaction_by_block(block=None, tx_index=0):
    if block and block > eth_get_block_number():
        raise ValueError("Block number should less than latest")
    return web3.eth.get_transaction_by_block(block_identifier=block, transaction_index=tx_index)


def eth_get_raw_transaction_by_block(block=None, tx_index=0):
    if block and block > eth_get_block_number():
        raise ValueError("Block number should less than latest")
    return web3.eth.get_raw_transaction_by_block(block_identifier=block, index=tx_index)


def eth_wait_for_transaction_receipt(tx, timeout=120, latency=0.1):
    return web3.eth.wait_for_transaction_receipt(transaction_hash=tx, timeout=timeout, poll_latency=latency)


def eth_get_transaction_receipt(tx):
    return web3.eth.get_transaction_receipt(transaction_hash=tx)


def eth_get_transaction_count(account, block=None):
    if block and block > eth_get_block_number():
        raise ValueError("Block number should less than latest")
    return web3.eth.get_transaction_count(account=web3.toChecksumAddress(account), block_identifier=block)


def eth_send_transaction(tx):
    return web3.eth.send_transaction(transaction=tx)


def eth_sign_transaction(tx):
    return web3.eth.sign_transaction(transaction=tx)


def eth_send_raw_transaction(tx):
    return web3.eth.send_raw_transaction(transaction=tx)


def eth_replace_transaction(tx_old_hash, tx_new):
    return web3.eth.replace_transaction(transaction_hash=tx_old_hash, new_transaction=tx_new)


def eth_modify_transaction(transaction_hash, **transaction_params):
    return web3.eth.modify_transaction(transaction_hash=transaction_hash, **transaction_params)


def eth_sign(account, data=None, hexstr=None, text=None):
    if not data and not hexstr and not text:
        raise ValueError("You should specify data or hexstr ot text")
    return web3.eth.sign(account=web3.toChecksumAddress(account), data=data, hexstr=hexstr, text=text)


def eth_sign_typed_data(account, json_message):
    return web3.eth.sign_typed_data(account=web3.toChecksumAddress(account), jsonMessage=json_message)


def eth_call(tx, block=None, state_override=None):
    if block and block > eth_get_block_number():
        raise ValueError("Block number should less than latest")
    return web3.eth.call(transaction=tx, block_identifier=block, state_override=state_override)


def eth_fee_history(blocks_amount, last_block, reward_percentiles=None):
    if last_block and last_block > eth_get_block_number():
        raise ValueError("Last block number should less than latest")
    return web3.eth.fee_history(block_count=blocks_amount, newest_block=last_block,
                                reward_percentiles=reward_percentiles)


def eth_estimate_gas(tx, block=None):
    if block and block > eth_get_block_number():
        raise ValueError("Last block number should less than latest")
    return web3.eth.estimate_gas(transaction=tx, block_identifier=block)


def eth_generate_gas_price(tx_params=None):
    return web3.eth.generate_gas_price(transaction_params=tx_params)


def eth_set_gas_price_strategy(gas_price_strategy):
    return web3.eth.set_gas_price_strategy(gas_price_strategy=gas_price_strategy)


# FILTERS


def eth_filter(filter_params):
    return web3.eth.filter(filter_params=filter_params)


def eth_get_filter_changes(filter_id):
    filter = web3.eth.filter()
    return web3.eth.get_filter_changes(filter=filter, filter_id=filter_id)


def eth_get_filter_logs(filter_id):
    filter = web3.eth.filter()
    return web3.eth.get_filter_logs(filter=filter, filter_id=filter_id)


def eth_uninstall_filter(filter_id):
    filter = web3.eth.filter()
    return web3.eth.uninstall_filter(filter=filter, filter_id=filter_id)


def eth_get_logs(filter_params):
    return web3.eth.get_logs(filter_params=filter_params)


def eth_submit_hashrate(hashrate, nodeid):
    return web3.eth.submit_hashrate(hashrate=hashrate, nodeid=nodeid)


def eth_submit_work(nonce, pow_hash, mix_digest):
    return web3.eth.submit_work(nonce=nonce, pow_hash=pow_hash, mix_digest=mix_digest)


# # CONTRACTS
#
# def eth_contract(address=None, contract_name=None, ContractFactoryClass=Contract, **contract_factory_kwargs):
#     return web3.eth.contract(address=address, contract_name=contract_name)

print(eth_get_balance('bigher.eth'))
# print(web3.eth.get_balance(account='bigher.eth'))!!!!!!!!!!!!!!
