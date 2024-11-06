numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbers1 = numbers[5:] # после неизвестного
numbers2 = numbers[:4] # до неизвестного
n = numbers2 + numbers1

l = len(n)
#print(l, 'len')

s = sum(n)
#print(s, 'sum')

ar = (s / (l+1))
#print(n)

numbers[4] = ar
print("Измененный список:", numbers)
