'''
№40
Обчислити суму парних елементів одновимірного масиву до першого
зустрінутого нульового елемента.
Дужак Андрій 122-Г
'''
import numpy as np
import random
a = np.zeros(10, dtype=int)
s = 0
for i in range(len(a)):
    a[i] = (random.randint(-10, 10)) 

for i in range(len(a)):
    if a[i] % 2 == 0:  # Перевірка умови
        if a[i] != 0:
            s += a[i]
        else:
            break
print(s)
print(a)
