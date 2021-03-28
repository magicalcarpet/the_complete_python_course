class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return "We're done here."


player1 = PlayerCharacter('Harry', 41)
print(player1.name)
print(player1.age)

player2 = PlayerCharacter('Thomas', 73)
print(player2.name)
print(player2.age)

print(player2.run())

player2.attack = 50

print(player2.attack)