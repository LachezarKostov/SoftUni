class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    # – if the amount is not an integer, raise ValueError with message
    # "please use int for amount"
    # otherwise, add the amount to the transactions

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account: "Account", amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")

        account._transactions.append(amount_to_add)
        return f"New balance: {account.balance}"

    # – if the transaction is possible, add it.
    # - if the balance becomes less than zero,
    # raise ValueError with message "sorry cannot go in debt!"and break the transaction.
    # Otherwise, complete it and return a message "New balance: {account_ballance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __add__(self, other):
        new_acc = Account(self.owner + "&" + other.owner, self.amount + other.amount)
        new_acc._transactions = self._transactions + other._transactions
        return new_acc



