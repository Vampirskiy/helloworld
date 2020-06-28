def print_sep(sep, sep_len):                           #Объявление функции с параметрами
    return sep * sep_len                               #Тело функции с параметрами
print(print_sep('*', 5))
sep1 = print_sep('-', 50)
sep2 = print_sep('*', 25)
text = 'Hello {} Funk {}' .format(sep1, sep2)
print(text)
print(print_sep('*', 3))