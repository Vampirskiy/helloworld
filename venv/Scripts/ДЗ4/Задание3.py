import random
name1 = input('Введите имя первого игрока: ')
name2 = input('Введите имя второго игрока: ')
har = { '01' : '50', '02' : '75', '03' : '25' , '04' : '15'}

def attack1():
    global har
    person1 = [name1, har['01'], har['03']]
    person2 = [name2, har['02'], har['04']]
    damage = random.randrange(0, int(person2[2]), 1)
    hel = int(person1[1])-damage
    har['01'] = str(hel)

def attack2():
    global har
    person1 = [name1, har['01'], har['03']]
    person2 = [name2, har['02'], har['04']]
    damage = random.randrange(0, int(person1[2]), 1)
    hel = int(person2[1])-damage
    har['02'] = str(hel)

attack1()
attack2()
attack1()
attack2()
attack1()
attack2()
attack1()
attack2()
attack1()
attack2()
a = har['01']
b = har['02']
print('Здоровье игрока {} {}, доровье игрока {} {}'.format(name1, a, name2, b))
