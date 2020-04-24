'''
№22
Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
Заповнення масиву здійснити випадковими числами від 5 до 500.
Дужак Андрій 122-Г
'''
import random
import numpy as np
a = np.zeros(10, dtype=int)
s = 1
for i in range(len(a)):
    a[i] = (random.randint(5, 500))
    if (a[i] % 3 == 0) and (a[i] % 9 == 0):  # Перевірка умови
        s *= a[i]
print(s)
