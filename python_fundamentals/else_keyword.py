cars = ['ok', 'ok', 'ok', 'faulty', 'ok', 'ok']

for status in cars:
    if status == 'faulty':
        print('Stopping the production line!')
        break
    print(f'This car is {status}.')
    print(f'Shipping new car to customer!')
else:
    print('All cars built successfully.')


# If we remove the faulty from the list

cars = ['ok', 'ok', 'ok', 'ok', 'ok']

for status in cars:
    if status == 'faulty':
        print('Stopping the production line!')
        break
    print(f'This car is {status}.')
    print(f'Shipping new car to customer!')
else:
    print('All cars built successfully.')

