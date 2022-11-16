#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos 
#quadrados dos elementos do vetor
vetA=[]
soma = 0
for i in range(10):
    vetA.append(int(input('Digite um valor: ')))
    vetA[i] = vetA[i]**2
    soma = sum(vetA)
print('A soma dos quadrados do vetor é {}'.format(soma))