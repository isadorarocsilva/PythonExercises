# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = pow(num, 0.5)
#raiz=num**(1/2)
print('\nNúmero: {}\nDobro do número: {}\nTriplo do número: {}\nRaiz quadrada do número: {}.\n'.format(num, dobro, triplo, raiz))