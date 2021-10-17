class SwapContract:

    def __init__(self, label, contract_hash, transfer_topic_hash):
        self.label = label
        self.contract_hash = contract_hash
        self.transfer_topic_hash = transfer_topic_hash

    def contract_match(self, transaction):
        return transaction.to == self.contract_hash

    # TODO : Is method topic always at the index 0 ?
    def is_transfer(self, transaction_receipt_log):
        topics = transaction_receipt_log['topics']
        return len(topics) != 0 and self.transfer_topic_hash == topics[0].hex()

    # def is_transfer(self, transaction_receipt_log):
    #     for topic in transaction_receipt_log['topics']:
    #         if topic.hex() == self.transfer_topic_hash:
    #             return True
    #     return False
