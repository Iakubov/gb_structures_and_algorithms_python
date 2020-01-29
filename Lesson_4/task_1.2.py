import timeit
import cProfile

# Определить, какое число в массиве встречается чаще всего.
import random


def max_freq(array):
    max_counter = 1
    num = array[0]
    for i in range(len(array)):
        counter = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                counter += 1
        if counter > max_counter:
            max_counter = counter
            num = array[i]

    return max_counter, num


size = 55
array = [random.randint(0, size * 10) for _ in range(size)]

print(timeit.timeit('max_freq(array)', number=100, globals=globals()))  # 0.00021010000000000126
print(timeit.timeit('max_freq(array)', number=100, globals=globals()))  # 0.0008928999999999986
print(timeit.timeit('max_freq(array)', number=100, globals=globals()))  # 0.002019
print(timeit.timeit('max_freq(array)', number=100, globals=globals()))  # 0.003564600000000001
print(timeit.timeit('max_freq(array)', number=100, globals=globals()))  # 0.00553
print(timeit.timeit('max_freq(array)', number=100, globals=globals()))  # 0.0081349

cProfile.run('max_freq(array)')  # 5000

#  5005 function calls in 0.639 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.639    0.639 <string>:1(<module>)
#         1    0.638    0.638    0.639    0.639 task_1.1.py:8(max_freq)
#         1    0.000    0.000    0.639    0.639 {built-in method builtins.exec}
#      5001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
