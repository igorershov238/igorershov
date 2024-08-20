# Д.З Сделать для макс значения
first_arg = int(input('Введите 1-е значение: '))
second_arg = int(input('Введите 2-е значение: '))
third_arg = int(input('Введите 3-е значение: '))
fourth_arg = int(input('Введите 4-е значение: '))

if first_arg <= second_arg and first_arg <= third_arg and first_arg <= fourth_arg:
    min = first_arg
    min_pos = 1
elif second_arg <= first_arg and second_arg <= third_arg and second_arg <= fourth_arg:
    min = second_arg
    min_pos = 2
elif third_arg <= first_arg and third_arg <= second_arg and third_arg <= fourth_arg:
    min = third_arg
    min_pos = 3
elif fourth_arg <= first_arg and fourth_arg <= second_arg and fourth_arg <= third_arg:
    min = fourth_arg
    min_pos = 4

print(f'min = {min}, pos = {min_pos}')

if first_arg >= second_arg and first_arg >= third_arg and first_arg >= fourth_arg:
    max = first_arg
    max_pos = 1
elif second_arg >= first_arg and second_arg >= third_arg and second_arg >= fourth_arg:
    max = second_arg
    max_pos = 2
elif third_arg >= first_arg and third_arg >= second_arg and third_arg >= fourth_arg:
    max = third_arg
    max_pos = 3
elif fourth_arg >= first_arg and fourth_arg >= second_arg and fourth_arg >= third_arg:
    max = fourth_arg
    max_pos = 4

print(f'max = {max}, pos = {max_pos}')
