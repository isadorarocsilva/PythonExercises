#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num = []
for x in range(3):
    num.append(int(input('Digite um número: ')))
print('\nO maior valor é {} e o menor é {}.\n'.format(max(num), min(num)))

#Outra forma:
#a = int(input('Digite um valor: '))
#b = int(input('Digite um valor: '))
#c = int(input('Digite um valor: '))
#menor = a
#if b < a and b < c:
#   menor = b
#if c < a and c < b:
#   menor = c
#maior = a
#if b > a and b > c:
#   maior = b
#if c > a and c > b:
#   maior = c
#print('O maior valor é {}.'.format(maior))
#print('O menor valor é {}.'.format(menor))