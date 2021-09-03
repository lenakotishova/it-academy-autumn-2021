# Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится.
# 0(zero), 1 (fib1), 1 (fib2), 2 (sum_), 3, 5, 8, 13, 21, 34, 55, 89, 144

n = int(input('n = '))
zero_item = 0
fib1, fib2 = 1, 1
while zero_item < n - 2:
       sum_ = fib1 + fib2
       fib1, fib2 = fib2, sum_
       zero_item += 1
print('{}-ое число Фибоначчи: {} '.format(n, sum_))