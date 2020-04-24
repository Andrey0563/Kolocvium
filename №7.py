'''
№7
Створіть масив А [1..12] за допомогою генератора випадкових чисел з
елементами від -20 до 10 і виведіть його на екран. Замініть всі від’ємні елементи
масиву числом 0.
Дужак Андрій 122-Г
'''
import numpy as np
import random
while True:
    a = np.zeros(12, dtype=int)
    for i in range(len(a)):
        a[i] = (random.randint(-20, 10))  
    print(a)

    for i in range(len(a) - 1):
        if a[i] < 0:  
            a[i] = 0
    print(a)

    answer = input("Повторити? так - 1, ні - інше")
    if answer == '1':
        continue
    else:
        break
