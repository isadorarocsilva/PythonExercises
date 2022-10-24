#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Ex.:
#Digite um número: 1834 
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

#primeira tentativa como string
from math import trunc
print('INICIO PRIMEIRA TENTATIVA COM STRING\n')
num = input('Digite um número: ')
if len(num) <= 4:
    list(num)
    if len(num) == 4:
        print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\n'.format(num[0], num[1], num[2], num[3]))
    if len(num) == 3:
        print('Unidade: {}\nDezena: {}\nCentena: {}\n'.format(num[0], num[1], num[2]))
    if len(num) == 2:
        print('Unidade: {}\nDezena: {}\n'.format(num[0], num[1]))
    if len(num) == 1:
        print('Unidade: {}\n'.format(num[0]))
    if len(num) == 0:
        print('Você digitou espaço.\n')
else:
    print('Digite um número menor que 9999.\n')
print('\nFIM TENTATIVA STRING\n\n')
#segunda tentativa como inteiro
print('INICIO SEGUNDA TENTATIVA COM INTEIRO\n')
numero = int(input('Digite um número: '))
if numero <= 9999 and numero > -1:
    if numero > 999:
        milhar = trunc(numero/1000)
        centena = trunc((numero - milhar*1000)/100)
        dezena = trunc((numero - milhar*1000 - centena*100)/10)
        unidade = numero - milhar*1000 - centena*100 - dezena*10
        print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\n'.format(unidade, dezena, centena, milhar))
    if numero > 99 and numero < 1000:
        centena = trunc(numero/100)
        dezena = trunc((numero - centena*100)/10)
        unidade = numero - centena*100 - dezena*10
        print('Unidade: {}\nDezena: {}\nCentena: {}\n'.format(unidade, dezena, centena))
    if numero > 9 and numero < 100:
        dezena = trunc(numero / 10)
        unidade = numero - dezena*10
        print('Unidade: {}\nDezena: {}\n'.format(unidade, dezena))
    if numero < 10:
        print('Unidade: {}\n'.format(numero))
else:
    print('Digite um número positivo menor que 9999.\n')
print('\nFIM TENTATIVA COM INTEIRO\n\n')

#Outra forma de resolver usando inteiro:
#num = int(input(numero: ))
#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10
#print('unidade: {}, dezena: {}, centena: {}, milhar: {}'.format(u, d, c, m))