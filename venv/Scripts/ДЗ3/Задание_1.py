import random
b = int(input('Введите верхний придел числа: '))
a = int(input('Введите нижний придел'))
user_number = False
while user == '=':
    number = random.randrange(a, b, 1)
    print(number)
    user = input('Это ваша цифра? ')
    if user == '=':
        user_number = True
        break
    elif user == '<':
        a = number + 1
    elif user == '>':
        b = number - 1
print('Конец')


