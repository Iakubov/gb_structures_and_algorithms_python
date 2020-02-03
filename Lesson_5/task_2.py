from collections import deque

a = deque(input('Введите первое число:'))
b = deque(input('Введите второе число:'))

hex_ = {
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}


def convert_from_hex(hex_num):
    converted_num = deque()
    for item in hex_num:
        if item in hex_:
            converted_num.append(hex_[item])
        else:
            converted_num.append(item)
    return converted_num


def hex_sum(x, y):
    sum_result = deque()
    result1 = deque()

    if len(x) < len(y):
        x, y = y, x

    y.extendleft('0' * (len(x) - len(y)))

    while len(x) != 0:
        sum_ = int(x.pop()) + int(y.pop())
        if sum_ > 16:
            sum_result.append(sum_ - 16)
            x.append(int(x.pop()) + 1)
        else:
            sum_result.append(sum_)

    for i in sum_result:
        for key, value in hex_.items():
            if i == value:
                result1.appendleft(key)
    return result1


print(f'Сумма чисел {a} + {b} = {hex_sum(convert_from_hex(a), convert_from_hex(b))}')
