#Exercício 4 : While + If/Else (com acumulador)
#Enunciado: Crie um programa de controle de estoque simples. O programa deve começar
#com 50 unidades de um produto. O usuário pode:
#(1) Adicionar unidades ao estoque
#(2) Remover unidades do estoque
#(3) Verificar estoque atual
#(4) Sair
#Não permita que o estoque fique negativo.

estoque = 50
acao = 10

while acao != 4:
    print('(1) adicionar')
    print('(2) remover')
    print('(3) verificar')
    print('(4) sair')
    acao = int(input(''))
    if acao >4:
        print('Ação invalida')
        break
    elif acao == 1:
        adicionar = int(input('Quantos produtos deseja adicionar? '))
        estoque = adicionar + estoque
    elif acao == 2:
        remover = int(input('Quanto você quer remover: '))
        estoque = estoque-remover
        if estoque < 0:
            print ('Impossivel realizar ação')
            estoque = estoque+remover

    elif acao == 3:
        print(f'O estoque atual é: {estoque}')
    else:
        print('Adeus 😭')
        break
    print('='*20)
    