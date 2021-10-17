class ERC20Contract:

    def __init__(self, label, contract):
        self.label = label
        self.contract = contract

    def is_about(self, transaction_receipt_log):
        return transaction_receipt_log['address'] == self.contract
