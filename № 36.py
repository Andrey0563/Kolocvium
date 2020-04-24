'''
№36
Знайти суму додатніх елементів лінійного масиву цілих чисел.
Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.
Дужак Андрій 122-Г
'''
import numpy as np
a = np.zeros(10, dtype=int)
s = 0
for i in range(len(a)):
    while True:
        try:
            a[i] = (int(input("Введыть елемент масиву: ")))
            break
        except ValueError:
            print('Тільки числа!')
    if a[i] > 0:  # Перевірка умови
        s += a[i]
print(s)
