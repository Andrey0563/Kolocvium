'''
№8
Створіть цілочисельний масив А [1..15] за допомогою генератора
випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте
найбільший елемент масиву і його індекс.
Дужак Андрій 122-Г
'''
import numpy as np
import random
while True:
    a = np.zeros(15, dtype=int)
    for i in range(len(a)):
        a[i] = (random.randint(-15, 30))  # Заповнення масиву
    print(a)

    n = 0
    ind = 0
    for i in range(len(a) - 1):
        if (a[i] > a[i+1]) and (a[i] > n):  # Пошук найбільшого елемента
            n = a[i]
            ind = i

    print(f'Найбільший елемент - {n}, з індексом - {ind}')

    answer = input("Повторити? так - 1, ні - інше")
    if answer == '1':
        continue
    else:
        break
