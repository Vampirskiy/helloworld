numbers = (5, 3, 4, 7, 8)
print(list(map(lambda x: x**2, numbers)))   #Выводим список квадратов чисел
print(list(map(lambda x: str(x), numbers))) #Приводим все числа к строке