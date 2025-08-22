#Enunciado: Escreva um programa que analise uma lista de números fornecida pelo usuário.
#Para cada número na lista, o programa deve determinar e exibir se ele é positivo, negativo
#ou zero. Além disso, no final, deve contar e mostrar a quantidade de números positivos,
#negativos e zeros encontrados.
#Exemplo de Saída:
#text
#Digite os números separados por espaço: 5 -2 0 8 -1 0
#5 é positivo.
#-2 é negativo.
#0 é zero.
#8 é positivo.
#-1 é negativo.
#0 é zero.
#Relatório:
#Positivos: 2
#Negativos: 2
#Zeros: 2

yn = 'a'
lista = []
pos = 0
neg = 0
zer = 0

addnum = int(input('Digite um numero: ')) 
lista.append(addnum)

while True:
    yn = input('Continuar: ')
    if yn == 'n':
        break
    addnum = int(input('Digite um numero: ')) 
    lista.append(addnum)

for num in lista:
    if num >= 1:
        pos +=1
    elif num < 0:
        neg += 1
    else:
        zer += 1
    
print(f'Positivos = {pos}\nNegativos = {neg}\nZero = {zer}')