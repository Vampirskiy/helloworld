n=None
while True:
    n = int(input('Введите число'))
    if n>=0 and n<=10:
        break
    print('Введите другое число')
print(n**2)
