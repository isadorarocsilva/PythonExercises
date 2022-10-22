#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
nome = []
for i in range(4):
    nome.append(input('Nome do aluno para sorteio: '))
random.shuffle(nome)
print('\nOrdem da apresentação: {}\n'.format(nome))