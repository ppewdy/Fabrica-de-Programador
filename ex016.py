idade = int(input('Digite sua idade: '))
if idade > 0 and idade < 13:
    print('criança')
elif idade >= 13 and idade < 18:
    print('adolescente')
else:
    print('adulto')