#Construa um algoritmo para calcular o volume de uma esfera de raio R, em que R é um dado 
#fornecido pelo usuário. Forneça como saída o resultado do cálculo executado.
from math import pi
raio = float(input('Valor do raio: '))
volume_esfera = 4/3*pi*(raio**3)
print('O volume é {:.1f}'.format(volume_esfera))