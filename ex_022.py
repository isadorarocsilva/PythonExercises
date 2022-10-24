#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas as letras minusculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome 
nome = input('Nome completo: ').strip()
print('Em maiúsculo:', nome.upper())
print('Em minúsculo:', nome.lower())
nome_sem_espaços_lista = nome.split()
nome_sem_espaços = ''.join(nome_sem_espaços_lista)
print('{} contém {} letras'.format(nome, len(nome_sem_espaços)))
print('{} contém {} letras'.format(nome_sem_espaços_lista[0], len(nome_sem_espaços_lista[0])))

#Outro formato da resolução:
#nome = input('Nome completo: ').strip()
#print('Em maiúsculo:', nome.upper())
#print('Em minúsculo:', nome.lower())
#print('O nome tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' '))) 