def chisla():
    numbers = []
    f = int(input('Введите количество чисел: '))
    for i in range(f):
        number = input('Введите число')
        numbers.append(number)
    print(max(numbers))
chisla()



