numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
none_index = numbers.index(None)

numbers_int = numbers[:none_index] + numbers[none_index + 1:]

list_lenght = len(numbers)

s = sum(numbers[:numbers.index(None)] + numbers[numbers.index(None) + 1:])


numbers[numbers.index(None)] = sum(numbers[:numbers.index(None)] + numbers[numbers.index(None) + 1:]) / len(numbers)
print("Измененный список:", numbers)
