'''
№29
Знайти кількість парних елементів одновимірного масиву до першого
зустрінутого числа рівного наперед заданому числу а.
Дужак Андрій 122-Г
'''
import numpy as np
import random
n = np.zeros(10, dtype=int)
a = int(input("Введіть будь-яке число: "))
k = 0
for i in range(len(n)):
    n[i] = (random.randint(0, 20))  # Заповнення масиву
for i in range(len(n)):
    if n[i] != a:
        if n[i] % 2 == 0:  # Пошук парного елемента
            k += 1
    else:
        break

print(n)
print(k)
