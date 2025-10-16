import requests
# GET
dados =  requests.get("https://68dea8ff898434f413559715.mockapi.io/Pedido")



result = dados.json()

for item in result:
    print(item.get('Prato'))

# =======================================


# prato = input('')
# bebida = input('')
# sobremesa = input('')
# mesa = int(input(''))

# pedido={
#     'Prato': prato,
#     'Bebida': bebida,
#     'Sobremesa': sobremesa,
#     'Mesa':mesa
# }

# dados = requests.post('https://68dea8ff898434f413559715.mockapi.io/Pedido',pedido)

# result = dados.json()

# print(result)

# Put

# prato = input('')
# bebida = input('')
# sobremesa = input('')
# mesa = int(input(''))

# pedido={
#     'Prato': prato,
#     'Bebida': bebida,
#     'Sobremesa': sobremesa,
#     'Mesa':mesa
# }

# requests.put('https://68dea8ff898434f413559715.mockapi.io/Pedido/',pedido)






# estoque = 50
# acao = 10

# while acao != 4:
#     print('(1) adicionar')
#     print('(2) remover')
#     print('(3) verificar')
#     print('(4) sair')
#     acao = int(input(''))
#     if acao >4:
#         print('Ação invalida')
#         break
#     elif acao == 1:
#         adicionar = int(input('Quantos produtos deseja adicionar? '))
#         estoque = adicionar + estoque
#     elif acao == 2:
#         remover = int(input('Quanto você quer remover: '))
#         estoque = estoque-remover
#         if estoque < 0:
#             print ('Impossivel realizar ação')
#             estoque = estoque+remover

#     elif acao == 3:
#         print(f'O estoque atual é: {estoque}')
#     else:
#         print('Adeus 😭')
#         break
#     print('='*20)

