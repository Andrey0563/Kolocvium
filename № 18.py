'''
№18
Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
масиву - 10. Заповнення масиву здійснити за допомогою клавіатури.
Дужак Андрій 122-Г
'''
import numpy as np
a = np.zeros(10, dtype=int)
s = 1
for i in range(len(a)):
    while True:
        try:
            a[i] = (int(input('Введіть елемент масиву: ')))
            break
        except ValueError:
            print("Тільки цілі числа")
    if a[i] < 0:  # Перевірка чи елемент менше 0
        s *= a[i]
print(s)
