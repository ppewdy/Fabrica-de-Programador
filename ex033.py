#Enunciado: Crie um programa que simule um caixa eletrônico simples. O programa deve
#iniciar com um saldo de R$ 1000,00. Ele deve apresentar um menu com as opções: (1)
#Sacar, (2) Depositar, (3) Ver Saldo e (4) Sair. O loop deve continuar até que o usuário
#escolha a opção 4. Para saques, não deve ser permitido sacar mais do que o saldo
#disponível.
#Exemplo de Saída:
#text
#Caixa Eletrônico
#(1) Sacar
#(2) Depositar
#(3) Ver Saldo
#(4) Sair
#Opção: 1
#Valor para sacar: 500
#Saque realizado com sucesso!
#...
#Opção: 4
#Obrigado por usar nossos serviços!

saldo = 1000
acao = 10
qqqqq6z5utryhfdvzsntrezrzezre
while acao != 4:
    print('(1) Sacar')
    print('(2) Depositar')
    print('(3) Ver Saldo')
    print('(4) Sair')
    acao = int(input(''))
    if acao >4:
        print('Açao invalida')
        break
    elif acao == 1:
        saque = float(input('Valor do saque: R$'))
        if saque > saldo:
            print('Saque a cima do valor disponivel!')
            break
        valor = valor - saque
    elif acao == 2:
        depositar = float(input('Quantos reais a depositar: R$'))
        saldo = saldo+depositar
    elif acao == 3:
        print(f'Seu saldo atual é: R${saldo}')
    else:
        print('Adeus 😭')
        break 
