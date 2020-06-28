print(abs(-7))                      #Модуль числа
numbers = [5, 15, 7, 1, -9, 0]
print(max(numbers))                 #Максимальное значение
print(min(numbers))                 #Минимальное значение
print(round(10.9872, 2))            #Округление до заданного периуда
print(sum(numbers))                 #Сумма
winners = ['Leo', 'Max', "Kate"]
for number, winner in enumerate(winners, 1):    #Для номера number, элемент winner из списка winners нумеруем с 1
    print(number, winner)