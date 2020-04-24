'''
№15
Знайти суму парних елементів масиву цілих чисел. Розмірність масиву -
20. Заповнення масиву здійснити випадковими числами від 100 до 200.
Дужак Андрій 122-Г
'''
import random
import numpy as np
a = np.zeros(20, dtype=int)
s = 0
for i in range(len(a)):
    a[i] = (random.randint(100, 200))
    if a[i] % 2 == 0:
        s += a[i]
print(s)
