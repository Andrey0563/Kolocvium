'''
№31
Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які потрапляють в інтервал від -2 до 10.
Дужак Андрій 122-Г
'''
import numpy as np
import random
a = np.zeros(10, dtype=int)
n = 0
s = 0
for i in range(len(a)):
    a[i] = (random.randint(-10, 20))

for i in range(len(a)):
    if -2 < a[i] < 10:  # Перевірка умови
        s += a[i]
        n += 1
s /= n  # Середнє арифметичне
print(f'{n:0.2f}')
