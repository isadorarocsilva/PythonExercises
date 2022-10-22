#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
#retângulo, calcule e mostre o comprimento da hipotenusa.
import math
cat_oposto = float(input('Cateto oposto: '))
cat_adjacente = float(input('Cateto adjacente: '))
hipotenusa = math.sqrt(pow(cat_oposto, 2)+pow(cat_adjacente, 2))
#outro modo de calcular a hipotenusa:
#hipotenusa = math.hypot(cat_oposto, cat_adjacente)
print('O comprimento da hipotenusa é {:.2f}\n'.format(hipotenusa))