sweet_dough = ["abcdefghijklmnopqrstuvwxyz".index(char) for char in 'donut']
print(sweet_dough)

two = [num / 2 for num in range(20)]
print(two)

donuts = [
    'Boston Cream',
    'Jelly',
    'Vanilla Cream',
    'Glazed',
    'Chocolate Cream'
]


cream_donuts = []
for donut in donuts:
    if 'Cream' in donut:
        cream_donuts.append(donut)

print(cream_donuts)

creamy_donuts = [donut for donut in donuts if 'Cream' in donut]
print(creamy_donuts)

lengthy_donut = [len(donut) for donut in donuts if 'Cream' in donut]
print(lengthy_donut)

creamless = [donut.split(" ")[0] for donut in donuts if 'Cream' in donut]
print(creamless)