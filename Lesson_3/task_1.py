# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

array = [0]*8
for item in range(2, 100):
    for number in range(2, 10):
        if item % number == 0:
            array[number - 2] += 1

for index, item in enumerate(array, 2):
    print(f'{index} = {item}')
