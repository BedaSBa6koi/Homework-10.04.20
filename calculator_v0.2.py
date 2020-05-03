#Переписанный калькулятор v0.2

print("Zero as an operation sign will terminate the program\n")
while True:
    s = input('Enter sign (+, -, *, /): ')
    if s == '0':
        print('Exit')
        break
    if s in ('+','-','*','/'):
        x = int(input('First number: ' ))
        y = int(input('Second number: '))
        if s == '+':
            print(x+y)
        elif s == '-':
            print(x-y)
        elif s == '*':
            print(x*y)
        elif s == '/':
            if y != 0:
                print(x/y)
            else:
                print("Сannot be divided by zero!")
    else:
        print("Invalid operation sign!")