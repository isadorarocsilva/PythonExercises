#Crie um programa que leia duas notas de um aluno e calcule 
#sua média, mostrando uma mensagem no final, de acordo com
#a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO
nota = []
cont = 0
for i in range(2):
    nota.append(float(input('Insira nota: ')))
    cont+=1
media = sum(nota) / cont
if media < 5:
    print('REPROVADO')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')