import requests

dados = requests.get('https://68dea8ff898434f413559715.mockapi.io/Pedido')

result = dados.json()

def delete(result):
    for item in result:
        id = item.get('id')
        pedido = item.get('Prato')
        if 'pizza' in pedido:
            requests.delete(f'https://68dea8ff898434f413559715.mockapi.io/Pedido/{id}')

delete()