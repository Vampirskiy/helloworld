print('Соревнования по Pyton')
count = int(input('Введите количество участников'))
i = count
members = []                                            #хранилище имен призеров
while i > 0:
    name = input('Кто занял {} место'.format(i))        #Вводим имена призеров
    members.append(name)                                #Запоминаем имена призеров
    i-=1                                                #Переходим к следующему призовому месту
print('В соревновании участвовали: ', sorted(members))  #Сортируем
members.reverse()                                       #Разворот списка в обратную сторону
result = members[:3]                                    #Срез 1-3 место
print('Победители: {}. Поздравляем!'.format(result))
