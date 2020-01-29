# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 15
MAX_ITEM = 30
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
num = array[0]
max_counter = 1

for i in range(len(array)):
    counter = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            counter += 1
    if counter > max_counter:
        max_counter = counter
        num = array[i]


print(f'Число {num} встречается {max_counter} раз')
