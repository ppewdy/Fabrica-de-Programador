palavra = input('Digite uma palavra: ')
contador = 0
vogais = 'aeiou'

for item in palavra:
    if item in vogais:
        contador += 1

print (contador)