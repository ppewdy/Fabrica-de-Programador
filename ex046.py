nome = input('digite o nome: ')
email= input('digite seu e-mail: ')
telefone = input('digite seu numero: ')

with open('contatos.txt', 'a') as arquivo:
    arquivo.write(nome+'|'+email+'|'+telefone)

with open('contatos.txt', 'r') as arquivo:
    content = arquivo.read()
    print(content)