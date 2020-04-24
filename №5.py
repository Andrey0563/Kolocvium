'''
№5
Створіть масив А [1..7] за допомогою генератора випадкових чисел і
виведіть його на екран. Збільште всі його елементи в 2 рази.
Дужак Андрій 122-Г
'''
import numpy as np
import random # Імпортуємо бібліотку Рандом
while True:
    a = np.zeros(7, dtype=int) # Заповнюємо масив нулями
    for i in range(len(a)):
        a[i] = (random.randint(-10, 10))  # Заповнюємо масив значеннями
    print(a)

    for i in range(len(a)):
        a[i] *= 2  # Збілшення елементів на 2
    print(a)

    answer = input("Повторити? так - 1, ні - інше")
    if answer == '1':
        continue
    else:
        break
