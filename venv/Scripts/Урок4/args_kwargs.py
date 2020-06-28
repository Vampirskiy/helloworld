def greeting(sey, *args):                #Функция с параметрами в виде картежа
    print(sey, args)
greeting('Hello', 'Leo')
greeting('Hello', 'Leo', 'Max')
greeting('Hello', 'Leo', 'Max', 'Kate')

def get_person(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
get_person(name='Leo', age=20, has_car=True)
