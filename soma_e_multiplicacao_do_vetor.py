# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e 
#os números.
vetor = []
soma = 0
multiplica = 1
for i in range(5):
    vetor.append(int(input('Digite um número: ')))
    soma = sum(vetor)
    multiplica *= vetor[i]
print('\nVetor: {}\nSoma: {}\nMultiplicação: {}'.format(vetor, soma, multiplica))