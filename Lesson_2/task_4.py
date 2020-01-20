# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def digit_counter(quantity, digit):
    counter = 0
    if quantity != 0:
        number = str(input('Введите ваше число: '))
        for i in number:
            if int(i) == digit:
                counter += 1
            else:
                continue
        return print(f'В вашем числе {counter}, цифр {digit}'), digit_counter(quantity - 1, digit)
    else:
        pass


digit_counter(3, 3)
