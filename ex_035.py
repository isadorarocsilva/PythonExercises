#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem 
#ou não formar um triângulo.
print('\nVamos construir um triângulo!\nPara isso, precisamos dos valores dos lados a, b e c do triângulo.')
a = float(input('Indique um valor para o lado a: '))
b = float(input('Indique um valor para o lado b: '))
c = float(input('Indique um valor para o lado c: '))

if(abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < a + b):
    print('\nVocê construiu um triângulo!\n')
else:
    print('\nOs lados inseridos não formam um triângulo!\n')