class Blockchain:

    def __init__(self):
        # stores block chain
        self.chain = list()
        # stores transactions
        self.current_transactions = list()

    # Creates and adds new blocks to chain
    def new_block(self):
        pass

    # Adds new transaction to existing transaction
    def new_transaction(self):
        pass

    @staticmethod
    def hash(block):
        pass

    # calls last block in chain
    def last_block(self):
        pass

    # register and add node to network
    def register_node(self):
        pass

    # check if following blocks in the chain are valid
    def valid_proof(self):
        pass
