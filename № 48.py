'''
№48
Наведено список прізвищ брокерів товарної біржі з N чоловік. Поміняйте
місцями прізвища брокерів: першого і останнього, другого і передостаннього, третього
з початку і третього від кінця і т.д.
Дужак Андрій 122-Г
'''
a = ['turner','castle','brige','digle','scott']
for i in range(len(a) // 2):  
    a[i], a[0-(1+i)] = a[0-(1+i)], a[i]
print(a)
