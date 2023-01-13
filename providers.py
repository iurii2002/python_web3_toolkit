from keys import INFURA_API_KEY

prividers_dict = {

    # INFURA

    # ETH L1 Blockchain
    'ETH_MAINNET': f'https://mainnet.infura.io/v3/{INFURA_API_KEY}',
    'ETH_GOERLI': f'https://goerli.infura.io/v3/{INFURA_API_KEY}',
    'ETH_SEPOLIA': f'https://sepolia.infura.io/v3/{INFURA_API_KEY}',

    # Arbitrum Ethereum L2/Rollup
    'ARB_MAINNET': f'https://arbitrum-mainnet.infura.io/v3/{INFURA_API_KEY}',
    'ARB_GOERLI': f'https://arbitrum-goerli.infura.io/v3/{INFURA_API_KEY}',

    # Optimism Ethereum L2/Rollup
    'OPTIMISM_MAINNET': f'https://optimism-mainnet.infura.io/v3/{INFURA_API_KEY}',
    'OPTIMISM_GOERLI': f'https://optimism-goerli.infura.io/v3/{INFURA_API_KEY}',

    # Avalanche C-Chain Ethereum L1
    'AVA_MAINNET': f'https://avalanche-mainnet.infura.io/v3/{INFURA_API_KEY}',
    'AVA_FUJI': f'https://avalanche-fuji.infura.io/v3/{INFURA_API_KEY}',

    # NEAR PoS L1
    'NEAR_MAINNET': f'https://near-mainnet.infura.io/v3/{INFURA_API_KEY}',
    'NEAR_TESTNET': f'https://near-testnet.infura.io/v3/{INFURA_API_KEY}',

    # Starknet Ethereum ZK-Rollup L2
    'STARKNET_MAINNET': f'https://starknet-mainnet.infura.io/v3/{INFURA_API_KEY}',
    'STARKNET_GOERLI1': f'https://starknet-goerli.infura.io/v3/{INFURA_API_KEY}',
    'STARKNET_GOERLI2': f'https://starknet-goerli2.infura.io/v3/{INFURA_API_KEY}',

    # Polygon Ethereum NFT Sidechain
    'POLYGON_MAINNET': f'https://polygon-mainnet.infura.io/v3/{INFURA_API_KEY}',
    'POLYGON_MUMBAI': f'https://polygon-mumbai.infura.io/v3/{INFURA_API_KEY}',

    # Palm
    'PALM_MAINNET': f'https://palm-mainnet.infura.io/v3/{INFURA_API_KEY}',
    'PALM_TESTNET': f'https://palm-testnet.infura.io/v3/{INFURA_API_KEY}',

    # Aurora Ethereum / Near Bridge
    'AURORA_MAINNET': f'https://aurora-mainnet.infura.io/v3/{INFURA_API_KEY}',
    'AURORA_TESTNET': f'https://aurora-testnet.infura.io/v3/{INFURA_API_KEY}',
}


def get_http_provider(chain):
    return prividers_dict[chain]
