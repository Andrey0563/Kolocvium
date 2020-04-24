'''
№9
З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
що протягом цього часу температура знижувалася. Визначте, о котрій годині було
вперше зафіксовано від'ємну температуру.
Дужак Андрій 122-Г
'''
import numpy as np
import random
t = np.zeros(13, dtype=int)
for i in range(len(t)):
    t[i] = (random.randint(-10, 10)) 

def buble_down(m):
    for k in range(0, len(m) - 1):
        for j in range(0, len(m) - 1 - k):
            if m[j] < m[j + 1]:
                m[j], m[j + 1] = m[j + 1], m[j]
    return m

t = buble_down(t)  # Сортуємо значення в порядку спадання(температура спадала)

for i in range(len(t)):
    if t[i] < 0:
        print(f"Вперше від'ємну температуру було зафіксовано о {i+8} годині")
        break
