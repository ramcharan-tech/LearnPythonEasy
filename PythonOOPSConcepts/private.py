class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._transactions = []   # protected (convention)
        self.__balance = balance  # private (name-mangled)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transactions.append(("deposit", amount))

    def get_balance(self):
        return self.__balance

acc = BankAccount("Alice", 1000)
acc.deposit(500)
print(acc.get_balance())  # 1500
# direct access discouraged:
print(acc._transactions)   # allowed but discouraged
# print(acc.__balance)    # AttributeError: name mangled
print(acc._BankAccount__balance)  # 1500 (possible but not advised)
