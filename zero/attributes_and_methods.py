class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name
            self.age = age

    def shout(self):
        return(f'My name is {self.name.upper()}')
        


player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter('Tina', 36)

# help(player1)
# help(list)

print(player1.name)
print(player2.membership)
print(player1.shout())