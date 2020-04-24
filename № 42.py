'''
№42
Підрахувати кількість елементів одновимірного масиву, для яких
виконується нерівність i*i<ai<i!
Дужак Андрій 122-Г
'''
import numpy as np
import random
a = np.zeros(20, dtype=int)
k = 0
for i in range(len(a)):
    a[i] = (random.randint(-10, 10)) 
    if i*i < a[i] < i:  # Перевірка умови
        k += 1
print(k)
