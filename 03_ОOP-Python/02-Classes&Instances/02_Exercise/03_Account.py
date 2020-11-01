from typing import Union


class Account:
    id: int
    name: str
    balance: int

    def __init__(self, id: int, name: str, balance: int = 0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount) -> Union[int, str]:
        if self.balance - amount < 0:
            return "Amount exceeded balance"

        self.balance -= amount
        return self.balance

    def info(self) -> str:
        return f"User {self.name} with account {self.id} has {self.balance} balance"

