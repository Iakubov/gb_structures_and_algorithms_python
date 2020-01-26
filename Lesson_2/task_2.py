# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def even_odd(a):
    a = str(a)
    even = 0
    odd = 0
    for i in a:
        if int(i) == 0:
            continue
        elif int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd
