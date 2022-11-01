#Leia um vetor de 10 elementos e calcule o maior e o menor valor.
print('\nVetor 1:\n')
vetor = []
for i in range(10):
    vetor.append(int(input('Digite número: ')))
    maior = max(vetor)
    menor = min(vetor)
print('\nO maior elemento do vetor é {} e o menor é {}.'.format(maior, menor))