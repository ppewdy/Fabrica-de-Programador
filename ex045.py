nome = input('digite seu nome: ')
try:
    with open('cliente.txt', 'r') as arquivo:
        arquivo.read()
except:
    criar = open('cliente.txt', 'x')