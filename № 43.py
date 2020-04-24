'''
№43
Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b.
Дужак Андрій 122-Г
'''
import numpy as np
import random
c = np.zeros(20, dtype=int)
a = int(input('Введіть значення а - '))
b = int(input('Введіть значення b - '))
w = False
for i in range(len(c)):
    c[i] = (random.randint(-20, 20))
    if c[i] % a == 0 and c[i] % b != 0:  # Перевірка умови
        w = True
print(w)
