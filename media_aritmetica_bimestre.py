#Construa um algoritmo que calcule a média aritmética entre quatro notas 
#bimestrais quaisquer fornecidas por um aluno (usuário)

aluno_lista=[]
media_bimestre=0
for i in range(4):
    aluno_lista.append(float(input('Insira a {}° nota:'.format(i+1))))
    if aluno_lista[i] <= 10 and aluno_lista[i] >= 0:  
        media_bimestre=sum(aluno_lista)/4
    else:
        print('Tem nota errada aí!\n')
        break
print('A sua média é {:.2f}.\n'.format(media_bimestre))