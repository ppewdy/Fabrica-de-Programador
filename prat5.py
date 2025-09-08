nome = input('digite o nome: ')
email = input('digite o e-mail: ')

with open('pessoas.txt', 'a') as arquivo:
    arquivo.write(nome+'|'+email+'\n')