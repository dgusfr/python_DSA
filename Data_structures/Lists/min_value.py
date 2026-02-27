my_array = [7, 12, 9, 4, 11, 3, 15]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print("Menor valor: ", minVal)
