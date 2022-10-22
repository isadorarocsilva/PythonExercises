#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente 
#desse ângulo.
import math
angulo = float(input('Ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}\n'.format(seno, cosseno, tangente))

#from math import radians, sin, cos, tan
#angulo = float(input('Ângulo: '))
#seno = sin(math.(angulo))
#cosseno = cos(radians(angulo))
#tangente = tan(radians(angulo))
#print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}\n'.format(seno, cosseno, tangente))
