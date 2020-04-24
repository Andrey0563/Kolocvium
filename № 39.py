'''
№39
Дані про температуру повітря і кількості опадів за декаду квітня
зберігаються в масивах. Визначити кількість опадів, що випали у вигляді дощу і у
вигляді снігу за цю декаду.
Дужак Андрій 122-Г
'''
import numpy as np
import random
t = np.zeros(30, dtype=int)
mm = np.zeros(30, dtype=int)
snow = 0
rain = 0
for i in range(30):
    t[i] = (random.randint(-15, 5))
    mm[i] = (random.randint(0, 30))
    if t[i] <= 0:  # Перевірка умови
        snow += mm[i]
    else:
        rain += mm[i]

print(f'Дощу випало - {rain}')
print(f'Снігу випало - {snow}')
