#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que 
#ajude ele, lendo o nome deles e escrevendo o nome escolhido.
import random
nome = []
for i in range(4):
    nome.append(input('Nome do aluno para sorteio: '))
print('\nAluno sorteado:{:^16}\n'.format(random.choice(nome)))