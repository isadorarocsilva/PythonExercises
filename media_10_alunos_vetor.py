#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a 
#média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0
notas_aluno = []
medias_aluno = []
contador_acima_media = 0
for i in range (10):
    for j in range(4):
        notas_aluno.append(float(input(f'Aluno {i+1} - {j+1}° Nota: ')))
        if notas_aluno[j] > 10 or notas_aluno[j] < 0:
            print('\nNota inválida! A nota está zerada no sistema, procure a direção.\n')
            break
    medias_aluno.append(sum(notas_aluno)/4)
    if medias_aluno[i] >= 7.0:
        contador_acima_media += 1
    notas_aluno = []
print(f'\nHá {contador_acima_media} alunos com média igual ou superior a sete.\n')