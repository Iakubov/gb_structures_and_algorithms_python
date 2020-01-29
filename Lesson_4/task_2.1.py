import timeit
import cProfile


def prime(n):
    j = 2
    count = 1
    while count < n:
        j += 1
        for i in range(2, j):
            if j % i == 0:
                break
        else:
            count += 1
    return j


print(timeit.timeit('prime(5)', number=100, globals=globals()))  # 0.00033869999999999734
print(timeit.timeit('prime(15)', number=100, globals=globals()))  # 0.0022567999999999998
print(timeit.timeit('prime(25)', number=100, globals=globals()))  # 0.0060874
print(timeit.timeit('prime(35)', number=100, globals=globals()))  # 0.011688200000000003
print(timeit.timeit('prime(45)', number=100, globals=globals()))  # 0.0191572
print(timeit.timeit('prime(55)', number=100, globals=globals()))  # 0.028475299999999995

cProfile.run('prime(5000)')


# 4 function calls in 5.463 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    5.463    5.463 <string>:1(<module>)
#         1    5.463    5.463    5.463    5.463 task_2.py:4(prime)
#         1    0.000    0.000    5.463    5.463 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
