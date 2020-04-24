'''
№14
Сформуйте лінійний масив дійсних чисел, елементи якого є відстанями,
пройденими тілом при вільному падінні на землю за 1, 2, ..., 10 с.
Дужак Андрій 122-Г
'''
import numpy as np
a = np.zeros(10, dtype=float)
for t in range(1, 11):
    s = (9.8 * t**2)/2  # Формула відстані при вільному падінні
    a[t-1] = s
print(a)
