'''
№35
Дано лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
спаданню.
Дужак Андрій 122-Г
'''
import numpy as np
import random
a = np.zeros(20, dtype=int)
for i in range(len(a)):
    a[i] = (random.randint(-20, 20)) 

for i in range(len(a)-1, -1, -1):
    if a[i] < a[i-1]:  # Перевірка умови
        if i == len(a):
            print("Масив впорядкований по спаданню")
        continue
    else:
        print("Масив не впорядкований по спаданню")
        break
