class BankAccount:
    def __init__(self, balance, interest_rate):
        self._balance = balance
        self._interest_rate = interest_rate
        self._transactions = []

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(f"Deposit {amount}")
            return print(f"The deposit of {amount} was successful")
        else:
            print("Enter a valid value")

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
            self._transactions.append(f"Withdraw {amount}")
            return print(f"The withdraw of {amount} was successful")
        else:
            print("Enter a valid value")

    def add_interest(self):
        if self._balance > 0:
            monthly_interest = self._balance * self._interest_rate
            self._balance += monthly_interest
            self._transactions.append(
                f"Accrual of monthly interest on a {monthly_interest} deposit "
            )
        else:
            print("You have no funds on your balance")

    def history(self):
        for transactions in self._transactions:
            print(transactions)
        print(f"Balance: {self._balance}")


account = BankAccount(5000, 0.05)
account.deposit(1000)
account.withdraw(379)
account.add_interest()
account.deposit(90000)
account.history()
