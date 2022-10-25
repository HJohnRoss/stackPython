kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}


class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team


player1 = Player(kevin["name"], kevin["age"],
                 kevin["position"], kevin["team"])
print([player1.name, player1.age, player1.position, player1.team])

player2 = Player(jason["name"], jason["age"],
                 jason["position"], jason["team"])
print([player2.name, player2.age, player2.position, player2.team])

player3 = Player(kyrie["name"], kyrie["age"],
                 kyrie["position"], kyrie["team"])
print([player3.name, player3.age, player3.position, player3.team])
