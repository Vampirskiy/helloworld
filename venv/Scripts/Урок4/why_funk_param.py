def my_filter(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(my_filter(numbers))