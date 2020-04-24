'''
№47
У лінійному масиві знайти максимальний елемент. Вставте порядковий
номер елемента за ним, пересунувши всі залишилися на одну позицію вправо.
Дужак Андрій 122-Г
'''
import numpy as np
import random
a = np.zeros(10, dtype=int)
for i in range(len(a)):
    a[i] = (random.randint(0, 100)) 
b = 0
Ind = 0
print(a)
for i in range(len(a)):
    if a[i] > a[i-1] and a[i] > b:
        b = a[i]
        Ind = i
print(b)
a[Ind+1:Ind+1] = [Ind]  # Вставка номера елемента
print(a)
