nome = input('digite o nome: ')
valor = input('digite o valor: ')
quantidade = input('digite a quantidade')

with open('cliente.txt' , 'a') as arquivo:
    arquivo.write(nome+ '|' +valor+ '|' +quantidade)