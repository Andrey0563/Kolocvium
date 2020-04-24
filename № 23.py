'''
№23
Знайти суму всіх елементів масиву цілих чисел, які менше середнього
арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 150 до 300.
Дужак Андрій 122-Г
'''
import numpy as np
import random
a = np.zeros(20, dtype=int)
s_arifm = 0
S = 0
for i in range(len(a)):
    a[i] = (random.randint(150, 300))
    s_arifm += a[i]
s_arifm /= len(a)  # Середнє арифметичне

for i in range(len(a)):
    if a[i] < s_arifm:  # Перевірка умови
        S += a[i]  # Сума
print(S)
