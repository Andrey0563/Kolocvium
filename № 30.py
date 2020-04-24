'''
№30
Oбчислити середнє арифметичне значення тих елементів одновимірного
масиву, які розташовані за першим по порядку мінімальним елементом.
Дужак Андрій 122-Г
'''
import numpy as np
import random
n = np.zeros(10, dtype=int)
s = 0
k = 0
for i in range(len(n)):
    n[i] = (random.randint(0, 20))

m = n[0]
mId = 0
for i in range(len(n) - 1):
    if (n[i] < n[i-1]) and (n[i] < m):
        mId = i

for i in range(mId+1, len(n)):  # Середнє арифметичне
    s += n[i]
    k += 1
s /= k
print(f'{s:0.2f}')
