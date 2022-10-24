#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
nome_cidade = input('Nome da cidade: ').strip().upper()
lista_nome_cidade = nome_cidade.split()
if lista_nome_cidade[0] == 'SANTO':
    print('O nome da cidade começa com Santo.\n')
else:
    print('O nome da cidade não começa com Santo.\n')

#Outra forma de resolver:
#nome = input('Cidade: ').strip()
#print(nome[:5].upper() == 'SANTO')