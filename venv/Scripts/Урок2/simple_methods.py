friends = ['Max', 'Leo', 'Kate']
print(friends)
print(len(friends)) #Подсчет количества друзей
friends.append('Ron') #Добавления нового элемента
print(friends.pop(2)) #Удаление и вывод элемента заданного индекса
print(friends)
friends.remove('Leo') #Удаление по значению
print(friends)
del friends[0] #Удаление по индексу
print(friends)
friends.clear() #Очистить весь список
print(friends)
