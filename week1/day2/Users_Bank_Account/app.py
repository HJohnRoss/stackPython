class BankAccount:

    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
            return self
        else:
            self.balance -= 5
            print(f"Insufficient funds: Charging a $5 fee")
            return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
            return self
        return self

# bank1 = BankAccount(0.2, 10)
# bank1.deposit(1).deposit(2).deposit(2).withdraw(
#     20).yield_interest().display_account_info()
# bank2 = BankAccount(0.1, 1004)
# bank2.deposit(1632).deposit(1875).withdraw(782).withdraw(976).withdraw(
#     703).withdraw(202).yield_interest().display_account_info()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    # other methods

    def make_deposit(self, amount):
        # your code here
