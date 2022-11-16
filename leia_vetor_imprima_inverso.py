#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no 
#seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida
idade = []
altura = []
for i in range(3):
    print('\nPessoa {}:'.format(i+1))
    idade.append(int(input('Idade: ')))
    altura.append(float(input('Altura: ')))
    if i == 2:
        print('\n Ordem inversa idade:')
        while i >= 0:
            print(idade[i])
            i-=1
        i = 2
        print('\n Ordem inversa altura:')
        while i >= 0:
            print(altura[i])
            i-=1