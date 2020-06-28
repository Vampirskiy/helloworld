max_things = {'телефон', 'бритва', 'рубашка', 'шорты'}
kate_things= {'телефон', 'шорты', 'зонтик', 'помада'}
print(max_things | kate_things)                            #Сложение
print(max_things & kate_things)                            #Пересечение
print(max_things - kate_things)                            #Вычетание
print(kate_things - max_things)