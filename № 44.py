'''
№44
Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
своїм номером і при цьому кратні 3.
Дужак Андрій 122-Г
'''
import numpy as np
import random
a = np.zeros(20, dtype=int)
b = 0
for i in range(len(a)):
    a[i] = (random.randint(-20, 20))
    if a[i] == i and a[i] % 3 == 0:  # Перевірка умови
        b += 1
print(b)
