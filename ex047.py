#with open("nota.txt", "w") as arquivo:
#    pass
aluno = input('Digite o nome do aluno: ').title().strip()
nota1 = float(input('digite a nota do 1° bimestre: '))
nota2 = float(input('digite a nota do 2° bimestre: '))
nota4 = float(input('digite a nota do 3° bimestre: '))
nota3 = float(input('digite a nota do 4° bimestre: '))

media = 0
while True:
    media = (nota1+nota2+nota3+nota4)/4
    
    if media > 6:
        resultado = '\033[32 mPassou\033[m'
        media = str(round(media, 2))
        with open('nota.txt', 'a') as arquivo:
            arquivo.write(aluno+' | '+resultado+' | '+media+'\n')
        with open('nota.txt', 'r') as arquivo:
            print(arquivo.read())
        break
    else:
        resultado = '\033[31mReprovou\033[m'
        media = str(round(media, 2))
        with open('nota.txt', 'a') as arquivo:
            arquivo.write(aluno+' | '+resultado+' | '+media+'\n')
        with open('nota.txt', 'r') as arquivo:
            print(arquivo.read())
        break
