#Exercício 1: If/Else (Múltiplas Condições)
#Enunciado: Escreva um programa que determine o preço do ingresso de cinema baseado
#na idade do cliente e se é estudante. As regras são:

#Crianças até 12 anos: R$ 8,00
#Estudantes (com carteirinha) de qualquer idade: R$ 12,00
#Idosos (65+ anos): R$ 10,00
#Adultos (13-64 anos) não estudantes: R$ 20,00
#O programa deve perguntar idade e se é estudante.
#Exemplo de Saída:
#text
#Digite sua idade: 18
#É estudante? (s/n): s
#Preço do ingresso: R$ 12.00

ingresso = 0
idade = int(input('Digite sua idade: '))
if idade < 13: #criança
    ingresso = 8.00
elif idade >= 13 and idade <= 64: #adulto
    ingresso = 20.00
else: #idoso
    ingresso = 10.00

#estuda = input('É estudante? (s/n) ')
#if estuda == 's':
#    ingresso = 12.00


print(f'O ingresso custara: {ingresso:.2f}')