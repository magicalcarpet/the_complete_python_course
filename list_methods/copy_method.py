units = ['meter', 'kilogram', 'second', 'ampere', 'kelvin', 'candela', 'mole']

copied_unit = units.copy()

print(units)
print(copied_unit)

units.remove('kelvin')
print(units)
print(copied_unit)

even_more_units = units[:]
print(even_more_units)