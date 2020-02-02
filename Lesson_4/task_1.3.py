import timeit
import cProfile

# Определить, какое число в массиве встречается чаще всего.
import random


def max_freq(array):
    counter = 0
    num = array[0]
    for i in array:
        max_counter = array.count(i)
        if max_counter > counter:
            counter = max_counter
            num = i
    return counter, num


size = 5000
array = [random.randint(0, size * 10) for _ in range(size)]

# print(timeit.timeit('max_freq(array)', number=100, globals=globals()))  # 6.559999999999899e-05
# print(timeit.timeit('max_freq(array)', number=100, globals=globals()))  # 0.00033460000000000087
# print(timeit.timeit('max_freq(array)', number=100, globals=globals()))  # 0.000867200000000002
# print(timeit.timeit('max_freq(array)', number=100, globals=globals()))  # 0.0015974999999999982
# print(timeit.timeit('max_freq(array)', number=100, globals=globals()))  # 0.0025610000000000008
# print(timeit.timeit('max_freq(array)', number=100, globals=globals()))  # 0.003852299999999996

cProfile.run('max_freq(array)')  # 5000

#  5004 function calls in 0.312 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.316    0.316 <string>:1(<module>)
#         1    0.001    0.001    0.316    0.316 task_1_2.py:8(max_freq)
#         1    0.000    0.000    0.316    0.316 {built-in method builtins.exec}
#      5000    0.315    0.000    0.315    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
