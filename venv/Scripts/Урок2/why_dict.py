friend = {
    'name': 'Max',
    'age': 23
}

print(friend['age'])
friend['has_car'] = True                                     #Добавление в словарь нового параметра
del friend['age']                                            #Удаление параметра из словаря
if 'has_car' in friend:
    print('есть машина')

for key in friend.keys():                                    #перебераем ключи словаря
    print(key)
    print(friend[key])

for key in friend:                                           #перебераем ключи словаря
    print(key)
    print(friend[key])

for val in friend.values():                                  #Перебераем значения ключей
    print(val)

for item in friend.items():                                  #Перебераем словарь в виде списка из картежей
    print(item)

for key, val in friend.items():                              #Перебераем в виде пары переменных
    print(key)
    print(val)
