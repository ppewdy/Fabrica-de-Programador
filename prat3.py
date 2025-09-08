num1 = input('')
num2 = input('')

try:
    num1 = int(num1)
    num2 = int(num1)
    print(f'A soma dos numeros é {num1+num2}')
except:
    print('digite um numero correto')