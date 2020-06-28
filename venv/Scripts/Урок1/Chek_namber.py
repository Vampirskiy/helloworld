number = 43
value = int(input('Введите число от 1 до 101'))
if value == number:
    print('Вы угадали!')
else:
    if value>number:
        print('Число меньше')
    else:
        print('Число больше')