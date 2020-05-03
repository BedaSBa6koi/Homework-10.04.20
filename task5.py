#Если вводимое число положительное, выводим "1", если отрицательное "-1", если 0 то выводим "0"

x = int(input('Enter the number: '))
if x > 0:
    print('1')
elif x < 0:
    print('-1')
else:
    x == 0
    print('0')
