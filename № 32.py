'''
№32
Змінній t привласнити значення істина, якщо в одновимірному масиві є
хоча б одне від’ємне і парне число.
Дужак Андрій 122-Г
'''
import numpy as np
import random
a = np.zeros(10, dtype=int)
t = False
for i in range(len(a)):
    a[i] = (random.randint(-20, 20))

for i in range(len(a)):  # Перевірка умови
    if a[i] < 0:
        for j in range(len(a)):
            if a[j] % 2 == 0:
                t = True
