from web3 import Web3

# Arbitrum Nova Chain ID - 42170
# Arbitrum One Chain ID - 42161

chain_details = {
    "chainId": 42161,
    "gas": 250000,
    "maxFeePerGas": Web3.toWei('0.1', 'gwei'),
    "maxPriorityFeePerGas": Web3.toWei('0.1', 'gwei'),
}