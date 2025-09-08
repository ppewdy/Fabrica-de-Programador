aluno = input()
nota1 = int(input())
nota2 = int(input())
nota3 = int(input())
media = 0
while True:
    media = (nota1+nota2+nota3)/3
    if media >= 7:
        passou = 'passou'
        with open('nota.txt', 'w') as arquivo:
            arquivo.write(aluno+'|'+passou)
            break
    else:
        passou = 'reprovou'
        with open('nota.txt', 'w') as arquivo:
            arquivo.write(aluno+'|'+passou)
        nota = open('nota.txt', 'r')
        print(nota)    
        break

