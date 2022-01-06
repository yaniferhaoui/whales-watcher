class SwapContract:

    def __init__(self, label, contract_hash, transfer_topic_hash, abi):
        self.label = label
        self.contract_hash = contract_hash
        self.transfer_topic_hash = transfer_topic_hash
        self.abi = abi

    def contract_match(self, transaction):
        return transaction.to == self.contract_hash

    def is_transfer(self, transaction_receipt_log):
        topics = transaction_receipt_log['topics']
        return len(topics) != 0 and self.transfer_topic_hash == topics[0].hex()
