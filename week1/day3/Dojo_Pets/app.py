class Ninja:

    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet_name, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet_name = pet_name
        self.action = pet

    def walk(self):
        self.action.play()
        print(f"{self.first_name} walks {self.pet_name}")
        return self

    def feed(self):
        print(f"{self.first_name} feeds {self.pet_name}")
        self.action.eat()
        return self

    def bathe(self):
        print(f"{self.first_name} bathe's {self.pet_name}")
        self.action.noise()
        return self

    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method


class Pet:

    def __init__(self, name, type, action, health, energy):
        self.name = name
        self.type = type
        self.action = action
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 2
        print(f"{self.name} sleeps | energy : {self.energy}")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} energy & health increased! new values: {self.energy} energy {self.health} health")
        return self

    def play(self):
        self.health += 5
        print(f"new total health: {self.health}")
        return self

    def noise(self):
        print({self.type})
        return self

    # implement __init__( name , type , tricks ):
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    # eat() - increases the pet's energy by 5 & health by 10
    # play() - increases the pet's health by 5
    # noise() - prints out the pet's sound


pet = Ninja("John", "Ross", "Cookie", "nibbles", "Mila", Pet(
    "Mila", "woof", "fetch", 100, 100).sleep()).walk().feed().bathe()
print(pet.pet_name)
