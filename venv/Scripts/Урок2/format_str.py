#фОРМАТИРОВАНИЕ СТРОК
name = 'Leo'
age = 30
#1 конкатинация
hello_str = 'Привет,  '+ name + ', тебе '+ str(age) + ' лет?'
print(hello_str)

#2%
hello_str = 'Привет %s тебе %d лет'%(name, age)
print(hello_str)

#3 format
hello_str = 'Привет {} тебе {} лет' .format(name, age)
print(hello_str)