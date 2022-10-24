class User:
    def __init__(self, first_name, last_name, email, age):
        self.first = first_name
        self.last = last_name
        self.mail = email
        self.num = age
        self.is_rewards_member = False
        self.gold_card_points = 300

    def display_info(self):
        print(f"{self.first}\n{self.last}\n{self.mail}\n{self.num}\n{self.is_rewards_member}\n{self.gold_card_points}")

    def enroll(self):
        if self.gold_card_points > 200:
            self.is_rewards_member = True
            return self
        else:
            self.is_rewards_member = False
            return self

    def spend_points(self, amount):
        if amount - self.gold_card_points < 0:
            self.gold_card_points -= amount
            return self
        else:
            return self


user1 = User("John", "Ross", "email@gmail.com", 20)
user2 = User("Kaija", "Pendergast", "dummy@gmail.com", 50)
user3 = User("Chandler", "McAdory", "commaAprentis@gmail.com", 25)
user1.spend_points(50).enroll().display_info()
user2.spend_points(80).enroll().display_info()
user3.spend_points(0).enroll().display_info()
