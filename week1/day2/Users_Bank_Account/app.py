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

    def transfer(self, amount, user):
        user.make_deposit(amount)
        self.withdraw(amount)
        return self


class User:

    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.bal = balance
        self.account = BankAccount(0.02, balance)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(f"{self.name}Deposited: {amount}")
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(f"{self.name}Withdrawed: {amount}")
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

    def money_transfer(self, amount, user):
        self.account.transfer(amount, user)
        return self


user1 = User("John", "email@test.com", 2137)
user2 = User("Jeffery", "gmail.com", 421)
user1.display_user_balance()
user2.money_transfer(213, user1).display_user_balance()
