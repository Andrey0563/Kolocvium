'''
№28
Знайти кількість парних елементів одновимірного масиву.
Дужак Андрій 122-Г
'''
import numpy as np
import random
a = np.zeros(10, dtype=int)
n = 0
for i in range(len(a)):
    a[i] = (random.randint(0, 20))
    if a[i] % 2 == 0:  # Пошук парного елемента
        n += 1
print(n)
