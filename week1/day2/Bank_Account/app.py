class BankAccount:
    # don't forget to add some default values for these parameters!
    # info = []

    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

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

    # @classmethod
    # def bank_info(cls, int_rate, balance):
    #     cls.info.append(int_rate)
    #     cls.info.append(balance)
    #     print(cls.info)


bank1 = BankAccount(0.2, 10)
bank1.deposit(1).deposit(2).deposit(2).withdraw(
    20).yield_interest().display_account_info()
bank2 = BankAccount(0.1, 1004)
bank2.deposit(1632).deposit(1875).withdraw(782).withdraw(976).withdraw(
    703).withdraw(202).yield_interest().display_account_info()
