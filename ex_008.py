#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input('Valor em metros: '))
centimetro = metro * 100
milimetro = metro * 1000
print('\n{:.2f}m equivale à {:.2f}cm e {:.2f}mm.\n'.format(metro, centimetro, milimetro))