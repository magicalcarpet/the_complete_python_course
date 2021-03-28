class Guitar:
    def __init__(self, wood):
        self.wood = wood


acoustic = Guitar('Mahogany')
electric = Guitar('Alder')

print(acoustic.wood)
print(electric.wood)