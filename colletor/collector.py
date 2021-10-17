from colletor.contract.ERC20Contract import ERC20Contract
from colletor.contract.SwapContract import SwapContract
from os import environ
from web3 import Web3

# Infura API Key
INFURA_PROJECT_ID = environ['INFURA_PROJECT_ID']

# List of AMM contract
SWAP_CONTRACTS = [
    SwapContract("Uniswap V2 : Router 2", "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D",
                 "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"),
    SwapContract("Uniswap V3 : Router", "0xE592427A0AEce92De3Edee1F18E0157C05861564",
                 "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"),
    SwapContract("SushiSwap : Router", "0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F",
                 "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef")
]

# List of ERC20 tokens to track
ERC20_CONTRACTS = [
    ERC20Contract("YFI - yearn.finance", "0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e")
]
START_FROM_BLOCK_INDEX = 10830904  # TODO : Change it to 0 to start from block 0

# Create Infura mainnet client API
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/" + str(INFURA_PROJECT_ID)))

# Iterate all blocks
for current_block_index in range(START_FROM_BLOCK_INDEX, web3.eth.get_block_number()):
    current_block = web3.eth.get_block(current_block_index, full_transactions=True)

    # Iterate all block transactions
    for transaction in current_block['transactions']:
        for swap_contract in SWAP_CONTRACTS:
            if swap_contract.contract_match(transaction):

                transaction_receipt = web3.eth.get_transaction_receipt(transaction['hash'])

                for erc20_contract in ERC20_CONTRACTS:
                    for log in transaction_receipt['logs']:
                        if swap_contract.is_transfer(log) and erc20_contract.is_about(log):
                            print("Current block: ", current_block, "\n\nTransaction: ", transaction, "\n\nLog: ", log)
                            # TODO : Store the event as BuySwap or SellSwap
