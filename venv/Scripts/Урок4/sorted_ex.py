numbers = [1, 5, 3, 5, 9, 7, 11]
print(sorted(numbers))
print(sorted(numbers, reverse=True))

names = ['Max', 'Alex', 'Kate']
print(sorted(names))

cities = [('Moskow', 20000), ('los-Vegas', 2000), ('Antwerpen', 4000)]
print(sorted(cities))

def by_count(city):
    return city[1]
print(sorted(cities, key=by_count, reverse=True))

print(sorted(cities, key=lambda city: city[1]))