import requests
from providers import ARBISCAN_TOKEN


def get_contract_abi(address):
    url = 'https://api.arbiscan.io/api?' \
          'module=contract&' \
          'action=getabi&' \
          f'address={address}&apikey={ARBISCAN_TOKEN}'
    return requests.get(url=url).json()['result']
