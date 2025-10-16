import requests

prato = ''
bebida= ''

acao = 0
while acao != 4:
    print ('      Ações\nRealizar Pedido - 1\nVer Pedido - 2\nRemover Item do Pedido - 3\nSair - 4')
    acao = int(input('Digite oque você quer fazer?'))

    if acao == 1:
        prato_qnt = int(input('Quantos pratos vai querer? '))
        prato = int(input('Numero do Prato: '))
        if prato == 1:
            prato = 'Pizza Marghrita'
        elif prato == 2:
            prato = 'Pizza Calabresa'
        elif prato == 3:
            prato = 'Pizza Portuguesa'
                
        bebida_qnt = int(input('Quantos bebidas vai querer?'))
        bebida = int(input('Numero da Bebida: '))
        if bebida == 1:
            bebida = 'Coca-Cola 1L'
        elif bebida == 2:
            bebida = 'Coca-Cola ZERO 1L'
        elif bebida == 3:
            bebida = 'Suco de Manga 500ml'
            
        mesa = int(input('Qual sua mesa? '))
        pedido={
            'Prato': prato,
            'Bebida': bebida,
            'qtd_Prato': prato_qnt,
            'qtd_Bebida': bebida_qnt,
            'Mesa': mesa
        }
        requests.post('https://68dea8ff898434f413559715.mockapi.io/Pedido',pedido)
    
    elif acao == 2:
        pedidos=requests.get('https://68dea8ff898434f413559715.mockapi.io/Pedido')
        print(pedidos.json())
    elif acao == 3:
        delped = int(input('Qual pedido deseja deletar'))
        requests.delete('https://68dea8ff898434f413559715.mockapi.io/delped')
        


