import emoji
import time

water = 300
milk = 200
coffee = 100
money = 0

cafe = ''

while True:
    print('='*30)
    print('What would you like?\n1) Expresso   $1,50\n2) Latte      $2,50\n3) Cappuccino $3,00\nOff to Cancel')
    print('='*30)

    while cafe != '1' and cafe != '2' and cafe != '3' and cafe != 'off' and cafe != 'report':
        cafe = input('Type the number:').lower()

    if cafe == 'off':
        break

# TODO: Report to show resource

    if cafe == 'report':
        print(f'Water: {water}ml')
        print(f'Milk: {milk}ml')
        print(f'Coffe: {coffee}g')
        print(f'Money: ${money}')
        cafe = ''
        continue

# TODO: CASH AND CHANGE!

    name = input('Name:')
    while True:
        try:
            cash = float(input('Insert the cash:'))
            break
        except ValueError:
            print('\033[31mInválido\033[m')


    print('='*30)

    if float(cafe) == 1:
        while cash < 1.5:
            print(f'Still missing ${(1.5 - cash):.2f}, {name}')
            while True:
                try:
                    cash += float(input('Insert the missing cash:'))
                    break
                except ValueError:
                    print('\033[31mInválido\033[m')
        if cash > 1.5:
            print(f'Your change ${(cash - 1.5):.2f} {emoji.emojize(":dollar_banknote:")}')
        type = 'Expresso'

    if float(cafe) == 2:
        while cash < 2.5:
            print(f'Still missing ${(2.5 - cash):.2f}, {name}')
            while True:
                try:
                    cash += float(input('Insert the missing cash:'))
                    break
                except ValueError:
                    print('\033[31mInválido\033[m')
        if cash > 2.5:
            print(f'Your change ${(cash - 2.5):.2f} {emoji.emojize(":dollar_banknote:")}')
        type = 'Latte'

    if float(cafe) == 3:
        while cash < 3:
            print(f'Still missing ${(3 - cash):.2f}, {name}')
            while True:
                try:
                    cash += float(input('Insert the missing cash:'))
                    break
                except ValueError:
                    print('\033[31mInválido\033[m')
        if cash > 3:
            print(f'Your change ${(cash - 3):.2f} {emoji.emojize(":dollar_banknote:")}')
        type = 'Cappuccino'


    # TODO: The storage

    if float(cafe) == 1:
        water -= 50
        coffee -= 18
        money += 1.5

    elif float(cafe) == 2:
        water -= 200
        coffee -= 24
        milk -= 150
        money += 2.5

    elif float(cafe) == 3:
        water -= 250
        coffee -= 24
        milk -= 100
        money += 3

    if water < 0 or coffee < 0 or milk < 0:
        print('\033[4:7mNot enough resource\033[m')
        break

    time.sleep(2)
    print(f'Here we go, {name}!\nYour {type} {emoji.emojize(":hot_beverage:")}')
    time.sleep(5)
    cafe = ''
