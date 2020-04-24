'''
№54
Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
однаковими значеннями.
Дужак Андрій 122-Г
'''
import numpy as np
import random
a = np.zeros(20, dtype=int)
for i in range(len(a)):
    a[i] = random.randint(0, 50) 
b = set(a)
if len(b) < len(a):  # Перевірка умови
    print(f"Масив {a} містить елемнти з однаковим значенням")
else:
    print('Елементів з однаковим значенням немає')
