'''
№4
Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
починаються з певної букви, яка вводиться з клавіатури.
Дужак Андрій (122-Г) 
'''
while True:
    a = ['Turner','Castle','Brige','Digle','Scott']
    letter = input('Введіть букву: ')
    for i in range(len(a)-1, -1, -1):
        if letter == a[i][0]:  # Порівняння першої букви 
            print(a[i])

    answer = input("Повторити? так - 1, ні - інше")
    if answer == '1':
        continue
    else:
        break
