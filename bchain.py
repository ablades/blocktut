class Blockchain(object):

    def __init__(self):
        # stores block chain
        self.chain = list()
        # stores transactions
        self.current_transactions = list()

        # Genesis Block
        self.new_block(previous_hash=1, proof=100)

    # creates and adds new blocks to chain
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        # reset transactions
        self.current_transactions = list()
        # log current block
        self.chain.append(block)

        return block

    # adds new transaction to existing transaction
    def new_transaction(self):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        }

        self.current_transactions.append(transaction)

        return self.last_block['index'] + 1

    # hash and sort dictonary
    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

    # calls last block in chain
    @property
    def last_block(self):
        return self.chain[:-1]

    # register and add node to network
    def register_node(self):
        pass

    # consensus algorithm
    def proof_of_work(self, last_proof):
        proof = 0

        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    # validates a block
    @staticmethod
    def valid_proof(self, last_proof, proof):
        guess = f'{last_proof}{proof}'

        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == "0000"
