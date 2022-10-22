#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o antecessor.

num = int(input('Digite um número: '))
ant = num - 1
suc = num + 1
print('\nO antecessor de {} é {}, e o sucessor é {}.'.format(num, ant, suc))
#print('\nO antecessor de {} é {}, e o sucessor é {}.'.format(num, num-1, num+1)')