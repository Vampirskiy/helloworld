import random
number = random.randint(1, 100)
#print(number)
user_number = None
levels = {1 : 10, 2 : 5, 3 : 3}
level = int(input('Введите уровень сложности от 1 до 3'))
count = 0
max_count = levels[level]
user_count = int(input('Введите количество пользователей'))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i+1}')
    users.append(user_name)
is_vinner = False
vinner_name = None
while not is_vinner:
    count += 1
    if count > max_count:
        print('Вы дибилы!')
        break
    print(f'Попытка номер {count}')
    for user in users:
        print(f'Ход пользователя {user}: ')
        user_number = int(input('Введите число от 1 до 100'))
        if user_number == number:
            is_vinner = True
            vinner_name = user
            break
        elif number < user_number:
            print('Введенное число больше загаданного')
        else:
            print('Введенное число меньше загаданного')
else:
    print(f'Победитель {vinner_name}')