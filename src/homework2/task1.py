#  Напишите программу, которая считает общую цену.
# Вводится M рублей и N копеек цена, а также количество S товара
# Посчитайте общую цену в рублях и копейках за L товаров.
# Пример:
# Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
# Output: Общая цена 9 рублей 60 копеек.

print('Пожалуйста, введите цену одной вещи ниже:')
M = int(input('рублей: '))
N = int(input('копеек: '))
S = int(input('Введите желаемое количество товара: '))
print('Цена одной вещи составила {0} рубля {1} копеек, посчитать {2} предмета'.format(M, N, S))
total_rubles = M * S
total_kopeck = N * S
while total_kopeck >= 100:
    total_kopeck = total_kopeck - 100
    total_rubles = total_rubles + 1
print('Цена составит {} рублей {} копеек'.format(total_rubles, total_kopeck))
