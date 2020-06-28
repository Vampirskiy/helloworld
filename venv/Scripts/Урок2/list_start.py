# можно объявить пустой список
empty_list = []
# можно объявить список и сразу его заполнить элементами
friends = ['Max', 'Leo', 'Kate']
# тип списка - list
print(type(friends))
# Как и в строке для списка доступны индексы (начиная с 0)
print('Второй друг: ', friends[1])
print('Первый друг с конца ', friends[-1])
#Можно применять срезы
print(friends[1:2])
print(friends[:2])
print(friends[1:])