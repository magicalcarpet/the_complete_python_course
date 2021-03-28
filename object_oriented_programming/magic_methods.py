class Student:
    def __init__(self, name):
        self.name = name


movies = ['The Matrix', 'Finding Nemo']
print(movies.__class__)
print(len(movies))


class Garage:
    def __init__(self):
        self.car = []

    def __len__(self):
        return len(self.car)

    def __getitem__(self, i):
        return self.car[i]
    
    def __repr__(self):
        return f'<Garage {self.car}>'

    def __str__(self):
        return f'Garage with {len(self)} cars'


ford = Garage()
print(ford.car)
ford.car.append('Fiesta')
ford.car.append('Focus')
print(ford.car)

print(len(ford))

print(ford[0])

for car in ford:
    print(car)

print(ford)


