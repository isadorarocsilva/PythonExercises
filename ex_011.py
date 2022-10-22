#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a 
#quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

altura = float(input('Insira altura em metro: '))
largura = float(input('Insira largura em metro: '))
area = largura * altura
litro_tinta = area / 2
print('\nA parede tem {}m², será preciso {}L de tinta.\n'.format(area, litro_tinta))