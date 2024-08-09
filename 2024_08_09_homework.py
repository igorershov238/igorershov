# Д.З Оператор if
#     Пользователь вводит значения 3 переменных: first_arg; second_arg; third_arg
# 1)  Найти минимальное значение из трёх введенных
# 2)  Найти максимальное значение из трёх введенных
# 3)  Среднее арифметическое, сумму, произведения
first_arg = int(input('Введите 1-е значение: '))
second_arg = int(input('Введите 2-е значение: '))
third_arg = int(input('Введите 3-е значение: '))
if first_arg < second_arg < third_arg:
    print('Минимальное значение:', first_arg)
if first_arg < third_arg < second_arg:
    print('Минимальное значение:', first_arg)
if second_arg < first_arg < third_arg:
    print('Минимальное значение:', second_arg)
if second_arg < third_arg < first_arg:
    print('Минимальное значение:', second_arg)
if third_arg < second_arg < first_arg:
    print('Минимальное значение:', third_arg)
if third_arg < first_arg < second_arg:
    print('Минимальное значение:', third_arg)
# 2)
if first_arg > second_arg > third_arg:
    print('Максимальное значение:', first_arg)
if first_arg > third_arg > second_arg:
    print('Максимальное значение:', first_arg)
if second_arg > first_arg > third_arg:
    print('Максимальное значение:', second_arg)
if second_arg > third_arg > first_arg:
    print('Максимальное значение:', second_arg)
if third_arg > second_arg > first_arg:
    print('Максимальное значение:', third_arg)
if third_arg > first_arg > second_arg:
    print('Максимальное значение:', third_arg)
# 3)
mid_ariph = (first_arg + second_arg + third_arg) / 3
print(f'Среднее арифметическое число: {mid_ariph:5.3}')
summa = first_arg + second_arg + third_arg
print('Сумма чисел: ', summa)
proizvedenie = first_arg * second_arg * third_arg
print('Произведение чисел: ', proizvedenie)
