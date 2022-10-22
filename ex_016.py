#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. 
#Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.
from math import trunc

num = float(input('Digite um número real: '))
print('O número {} tem a parte inteira {}\n'.format(num, trunc(num)))

#outro modo sem precisar importar math:
#num = float(input('Digite um número real: '))
#print('O número {} tem a parte {} inteira {}\n'.format(num, int(num)))