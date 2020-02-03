from collections import namedtuple

Company = namedtuple('Company', 'name, profit')
companies = []
total_profit = 0

number_of_companies = int(input('Введите кол-во предприятий: '))

for i in range(1, number_of_companies + 1):
    name = input(f'Введите название {i}-ого предприятия: ')
    first_quarter = int(input('Введите прибыль за 1-ый квартал: '))
    second_quarter = int(input('Введите прибыль за 2-ой квартал: '))
    third_quarter = int(input('Введите прибыль за 3-ий квартал: '))
    fourth_quarter = int(input('Введите прибыль за 4-ый квартал: '))
    total_profit += first_quarter + second_quarter + third_quarter + fourth_quarter
    company = Company(name=name, profit=first_quarter + second_quarter + third_quarter + fourth_quarter)
    companies.append(company)


for company in companies:
    print(f'Средняя прибыль всех компаний = {total_profit / number_of_companies}')
    if company.profit > (total_profit / number_of_companies):
        print(f'Компания - {company.name}, заработала за год  = {company.profit}, что является выше среднего')
    else:
        print(f'Компания - {company.name}, заработала за год = {company.profit}, что является ниже среднего')
