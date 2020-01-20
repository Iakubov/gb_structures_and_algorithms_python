# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

number = int(input('Введите число: '))
gr_number = 0
summ = 0

while number != 0:
    if number > gr_number:
        gr_number = number
    number = int(input('Введите число: '))
else:
    for i in str(gr_number):
        summ += int(i)
    print(gr_number, summ)
