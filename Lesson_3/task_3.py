# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MAX_ITEM = 30
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
min_ = array[0]
max_ = array[0]

for item in range(len(array)):
    if array[item] < array[min_]:
        min_ = item
    elif array[item] > array[max_]:
        max_ = item

array[max_], array[min_] = array[min_], array[max_]

print(array)