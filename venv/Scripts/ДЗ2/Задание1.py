my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
for number in my_list_1[:]:                          #Двигаемся по срезу списка my_list_1
    if number in my_list_2:                          #Если number есть в списке my_list_2
        my_list_2.remove(number)                     #Мы это число будем удалять из списка my_list_1
print(my_list_1)

