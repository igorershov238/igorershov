# Пользователь вводит 3 целых переменных a, b, c
# поменять значения этих переменных по кругу:
# a --> b
# b --> c
# c --> a
# 1.Вар решения: С использованием доп переменной
# 2.Вар решения: Без использования доп переменной, с применением арифметических операций (+ - * /)
a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
b = b + a;
a = b - a;
b = b - a;
c, a = a, c
print('a =',a,'b =',b,'c =',c)