cyties = {'Las Vegas', 'Paris', 'Moscow'}
cyties.add('Burma')                                      #Добавление элемента в множество
cyties.remove('Moscow')
print(len(cyties), cyties)
print('Paris' in cyties)
for cyti in cyties:
    print(cyti)