'''
№16
Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.
Дужак Андрій 122-Г
'''
import numpy as np
import random
a = np.zeros(15, dtype=int)
s = 1
for i in range(len(a)):
    a[i] = (random.randint(10, 50))
    if a[i] % 7 == 0:
        s *= a[i]
print(s)
