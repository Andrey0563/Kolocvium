'''
№33
Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
Дужак Андрій 122-Г
'''
import numpy as np
import random
a = np.zeros(20, dtype=int)
s = 1
for i in range(len(a)):
    a[i] = (random.randint(-10, 10))
    if a[i] != 0:  # Перевірка чи елемент не дорівнює 0
        s *= a[i]
print(s)
