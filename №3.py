'''
№3
Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком,
починаючи з останнього.
Дужак Андрій (122-Г) 
'''
while True:
    a = ['Turner','Castle','Brige','Digle','Scott']
    for i in range(len(a)-1, -1, -1):
        print(a[i])

    answer = input("Повторити? так - 1, ні - інше")
    if answer == '1':
        continue
    else:
        break


