import random
name1 = input('Введите имя первого игрока: ')
name2 = input('Введите имя второго игрока: ')
har = { '01' : '50', '02' : '75', '03' : '25' , '04' : '15', '05' : '1.2', '06' : '1.4'}

def attack1():
    global har
    person1 = [name1, har['01'], har['03'], har['05']]
    person2 = [name2, har['02'], har['04'], har['06']]
    damage = random.randrange(0, int(person2[2]), 1)
    def armor(damage):
        damage = damage//float(person1[3])
        return damage
    armor(damage)
    hel = int(person1[1])-int(damage)
    har['01'] = str(hel)

def attack2():
    global har
    person1 = [name1, har['01'], har['03'], har['05']]
    person2 = [name2, har['02'], har['04'], har['06']]
    damage = (random.randrange(0, int(person1[2]), 1))
    def armor(damage):
        damage = damage//float(person2[3])
        return damage
    armor(damage)
    hel = int(person2[1])-damage
    har['02'] = str(hel)

attack1()
print('Здоровье игрока {} {}.'.format(name1, har['01']))
attack2()
print('Здоровье игрока {} {}.'.format(name2, har['02']))
attack1()
print('Здоровье игрока {} {}.'.format(name1, har['01']))
attack2()
print('Здоровье игрока {} {}.'.format(name2, har['02']))
attack1()
print('Здоровье игрока {} {}.'.format(name1, har['01']))
attack2()
print('Здоровье игрока {} {}.'.format(name2, har['02']))
attack1()
print('Здоровье игрока {} {}.'.format(name1, har['01']))
attack2()
print('Здоровье игрока {} {}.'.format(name2, har['02']))
attack1()
print('Здоровье игрока {} {}.'.format(name1, har['01']))
attack2()
print('Здоровье игрока {} {}.'.format(name2, har['02']))
