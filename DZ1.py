# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396

import random

N = random.randint(10, 10000)
#N = 132
temp1 = str(N)
temp2 = str(N)
i = 1
while i < 3:
    temp2 = temp1 + temp2
    N += int(temp2)
    i += 1

print(N)
