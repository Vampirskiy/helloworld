from random import randint, choice, sample, shuffle
#Загадать случайное число
print(randint(0, 100))
#Выбрать победителя из списка
players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
print(choice(players))
#Выбрать трех победителей из списка
print(sample(players, 3))
#перемешать карты в списке
cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
shuffle(cards)
print(cards)