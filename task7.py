#Факториал вводимого числа

n = int(input('Enter the number: '))
 
fact = 1

while n > 1:
    fact *= n
    n -= 1

print('Factorial of this number =', fact)
