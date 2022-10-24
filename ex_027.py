#Faça um programa que leia o nome completo de uma pessoa, mostando em seguida o primeiro e 
#o último nome separadamente.
#Ex: Ana Maria Braga
#primeiro = Ana
#último = Braga
nome = input('Nome completo: ').strip()
lista_nome = nome.split()
tam_nome = len(lista_nome)
primeiro_nome = lista_nome[0]
ultimo_nome = lista_nome[tam_nome-1]
print('Primeiro nome: {}\nÚltimo nome: {}\n'.format(primeiro_nome, ultimo_nome))

#Outra forma:
#n = input('Nome completo: ').strip()
#nome = n.split()
#print('Seu primeiro nome é {}'.format(nome[0]))
#print('Seu último nome é {}'.format(nome[len(nome)-1]))