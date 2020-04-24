'''
№13
Створіть масив з 15 цілочисельних елементів і визначте серед них
мінімальне значення.
Дужак Андрій 122-Г
'''
import numpy as np
import random
a = np.zeros(15, dtype=int)
for i in range(len(a)):
    a[i] = (random.randint(-20, 20))
print(a)
m = min(a)
print(f'Найменше значення - {m}')
