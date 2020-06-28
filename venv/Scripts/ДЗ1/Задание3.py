name = input('Введите ФИО')
age = int(input('сколько вам лет?'))
ves = int(input('какой ваш вес?'))
if age<=30 and (ves>=50 and ves<=120):
    print(name, age, 'лет', ves, 'кг', 'Пациент в хорошем состоянии')
elif age>30 and age<40 and (ves<50 or ves>120):
    print(name, age, 'лет', ves, 'кг', 'Пациенту требуется занятся собой')
elif age>40 and (ves < 50 or ves>120):
    print(name, age, 'лет', ves, 'кг', 'Пациенту требуется врачебный осмотр')
else:
    print(name, 'идите на хуй!')


