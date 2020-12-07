class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    def __reversed__(self):
        return self[::-1]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __add__(self, other):
        owner = f'{self.owner}&{other.owner}'
        start_amount = self.amount + other.amount
        acc = Account(owner, start_amount)
        for t in self._transactions + other._transactions:
            print(t)
            acc.add_transaction(t)
        return acc

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(acc, amount_to_add):
        acc.add_transaction(amount_to_add)
        if acc.balance < 0:
            acc._transactions.pop()
            raise ValueError('sorry cannot go in debt!')
        return f'New balance: {acc.balance}'


