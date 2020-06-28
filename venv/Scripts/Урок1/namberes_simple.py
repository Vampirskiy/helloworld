#вывод чисел от 0 до 100
#вывод чисел от 0 до n
#вывод четных чисел от 0 до n
number=int(input('Введите наименьшее число'))
n=int(input('Введите наибольшее число'))
while number <= n:
    if number%2!=0:
        number+=1   # nummber = number + 1
        continue
    print(number)
    number += 1    # nummber = number + 1

