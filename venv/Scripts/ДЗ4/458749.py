import random
har = { '01' : '50', '02' : '75', '03' : '25' , '04' : '15', '05' : '1.2', '06' : '1.4'}
name1 = input('Введите имя первого игрока: ')
name2 = input('Введите имя первого игрока: ')
person1 = [name1, har['01'], har['03'], har['05']]
person2 = [name2, har['02'], har['04'], har['06']]
damage = int(person2[2])
def armor(armor):
    damage1 = damage // armor
    return damage1
    print(damage1)
armor(2)
print(damage1)
hel = int(person1[1]) - damage1
har['01'] = str(hel)
print(hel)