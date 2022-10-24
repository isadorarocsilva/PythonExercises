#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.
nome = input('Nome completo: ').strip().upper()
if 'SILVA' in nome:
    print('A pessoa tem Silva no nome.\n')
else:
    print('A pessoa não tem Silva nome.\n')

#Outra forma:
#nome = input('Seu nome completo: ').strip()
#print('Tem Silva no nome? {}'.format('silva' in nome.lower()))