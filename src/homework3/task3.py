"""
Tuple practice
Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы
последовательно выводились значения 1, 2, 3.
Убедитесь что len() исходного кортежа возвращает 1.
"""

# Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
list1 = ['a', 'b', 'c']
tuple1 = tuple(list1)
print('Tuple: ', tuple1, 'Type: ', type(tuple1))

# Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
tuple11 = 'a', 'b', 'c'
list11 = list(tuple11)
print('List: ', list11, 'type: ', type(list11))

# Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
a, b, c = 'a', 2, 'python'
print('b = {}; c = {}; a = {}'.format(b, c, a))

# Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы
# последовательно выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.
n = 1, 2, 3
tuple_new = n,
print('tuple_new = ', tuple_new, 'len(tuple_new) = ', len(tuple_new))