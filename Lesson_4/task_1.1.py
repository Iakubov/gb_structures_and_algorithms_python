import timeit
import cProfile

# Определить, какое число в массиве встречается чаще всего.
import random


def max_freq(size):
    array = [random.randint(0, size * 10) for _ in range(size)]
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

    return max_counter, num


print(timeit.timeit('max_freq(5)', number=100, globals=globals()))  # 0.0006946999999999995
print(timeit.timeit('max_freq(15)', number=100, globals=globals()))  # 0.0022828000000000015
print(timeit.timeit('max_freq(25)', number=100, globals=globals()))  # 0.004122500000000001
print(timeit.timeit('max_freq(35)', number=100, globals=globals()))  # 0.006816200000000001
print(timeit.timeit('max_freq(45)', number=100, globals=globals()))  # 0.009552600000000001
print(timeit.timeit('max_freq(55)', number=100, globals=globals()))  # 0.014489699999999994

cProfile.run('max_freq(5000)')

# 31579 function calls in 0.653 seconds
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.653    0.653 <string>:1(<module>)
#      5000    0.002    0.000    0.005    0.000 random.py:174(randrange)
#      5000    0.001    0.000    0.006    0.000 random.py:218(randint)
#      5000    0.002    0.000    0.003    0.000 random.py:224(_randbelow)
#         1    0.645    0.645    0.653    0.653 task_1.py:8(max_freq)
#         1    0.001    0.001    0.007    0.007 task_1.py:9(<listcomp>)
#         1    0.000    0.000    0.653    0.653 {built-in method builtins.exec}
#      5001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      5000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      6573    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}