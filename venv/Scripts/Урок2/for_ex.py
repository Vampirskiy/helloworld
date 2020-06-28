friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'guest', 'user')
if 'Max' in friends:                 #Поиск Мах в массиве френдс
    print('У меня есть этот друг')
if 'M' in friend_name:               #Поиск М в слове Мах
    print('Буква М есть в имени друга')

#while
i=0
while i < len(friends):    #пока число меньше количества друзей
    friend = friends[i]    #присваивание переменной имени по индексу i
    print(friend)
    i+=1                   #шаг цикла

#For
for friend in friends:
    print(friend)