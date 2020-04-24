'''
№1
Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в
один рядок через кому. Отримайте для масиву середнє арифметичне.
Дужак Андрій (122-Г) 
'''
import numpy as np
while True:
    a = np.zeros(5, dtype=int) # Заповнюємо нулями
    S = 0
    for i in range(len(a)):
        while True:
            try:
                a[i] = (int(input('Введіть значення: ')))
                break
            except ValueError:
                print('Тільки цілі числа')
        S += a[i]  # Виведення сер. арифметичного
    S /= 5  # Середнє арифметичне
    print(f'Cереднє арифметичне = {S}')
    for i in a:
        print(i, end=',')

    answer = input("Повторити? так - 1, ні - інше")
    if answer == '1':
        continue
    else:
        break
