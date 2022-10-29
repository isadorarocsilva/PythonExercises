#Construa um algoritmo que calcule a quantidade de latas de tinta necessárias e o custo para pintar 
#tanques cilíndricos de combustível, em que são fornecidos a altura e o raio desse cilindro. 
#Sabendo que:
#A lata de tinta custa R$ 50,00
#Cada lata contém 5 litros
#Cada litro de tinta pinta 3 metros quadrados
#Dados de saída: custo (C) e quantidade de latas cheias (QTDE)
#A = 2πr(r + h)
from math import pi, ceil
altura_cilindro = float(input('Altura em metros: '))
raio_cilindro = float(input('Raio em metros: '))
area_cilindro = 2 * pi * raio_cilindro * (raio_cilindro + altura_cilindro) #A = [m²]
litros_tinta_usados = area_cilindro / 3
total_latas = ceil(litros_tinta_usados / 5)
custo_tinta = 50 * total_latas
print('\nPara essa peça, será necessário usar {} latas, que custará R${:.2f}\n'.format(total_latas, custo_tinta))