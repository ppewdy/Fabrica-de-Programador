import streamlit as st

# conls = st.columns(4)

# conls[0].image('theking.jpg')
# conls[0].title('sun king')
# conls[1].image('theaustralianking.jpg')
# conls[1].title('australia king')
# conls[2].image('theegypcianking.jpg')
# conls[2].title('egypt king')
# conls[3].image('thewestking.jpg')
# conls[3].title('west king')


# lista = st.columns(4)
# cont = 0

# with lista[0]:
#     st.write('Coluna 1')

#     nome=st.text_input('Digite seu nome')
#     if st.button('Mostrar'):
#         st.write(f'Seu nome é {nome}')
    
#         if nome == 'Pedro':
#             st.success('Bem vindo Pedro')
#             cont += 1
#         else:
#             st.error('Quem é você?')



# with lista[1]:
#     st.write('Coluna 2')
#     email=st.text_input('Digite seu email')
#     if st.button('Mostrar nome'):
#         st.write(f'Seu email é {email}')
#         if email == 'mr.peterfarinha':
#             st.success('Bem vindo Pedro')
#         else:
#             st.error('Quem é você?')



# with lista[2]:
#     st.write('Coluna 3')
#     telefone=st.text_input('Digite seu telefone')
#     if st.button('Mostrar telefone'):
#         st.write(f'Seu telefone é {telefone}')   
#         if telefone == '11968183873':
#             st.success('Bem vindo Pedro')
#         else:
#             st.error('Quem é você?')


# with lista[3]:
#     st.write('Coluna 4')
#     endereco=st.text_input('Digite seu endereço')
#     if st.button('Mostrar endereço'):
#         st.write(f'Seu endereço é {endereco}')
#         if endereco == 'Rua porto rico':
#             st.success('Bem vindo Pedro')
#         else:
#             st.error('Quem é você?')




email = st.text_input('Digite seu email')
senha = st.text_input('Digite sua senha')
telefone = st.text_input('Digite seu telefone')


if st.button('Enviar'):
    if email == 'mr.peterfarinha' and senha == '123456' and int (telefone) == 11968183873:
        st.success('Email e senha corretos')
    else:
        st.error('Email ou senha incorretos')
    