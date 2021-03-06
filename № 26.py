'''
№26
Напишіть програму аналізу значень температури хворого за добу:
визначте мінімальне і максимальне значення, середнє арифметичне. Заміри
температури виробляються шість раз на добу і результати вводяться з клавіатури у
масив T.
Дужак Андрій 122-Г
'''
import numpy as np
T = np.zeros(6, dtype=float)
s_arifm = 0
for i in range(len(T)):
    T[i] = (float(input("Введіть значення температури: ")))  # Заповнення масиву
    s_arifm += T[i]
s_arifm /= len(T)  # Середня температура
m1 = max(T)  # Максимальна температура
m2 = min(T)  # Мінімальна температура
print(f' Середня температура - {s_arifm:0.2f}\n Максимальна температура - {m1} \n Мінімальна температура - {m2}')
