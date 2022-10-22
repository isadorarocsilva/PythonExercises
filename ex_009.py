#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('\nDigite um número para ver a sua tabuada de 1 a 10: '))
mult = 0
for x in range(1, 11):
    mult = num * x
    print('{:^10}x{:^11}={:^11}'.format(num, x, mult))
print('\n')