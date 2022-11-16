#Refaça o desafio dos triângulos acrescentando o recurso 
#de mostrar que tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes
a = float(input('Indique um valor para o lado a: '))
b = float(input('Indique um valor para o lado b: '))
c = float(input('Indique um valor para o lado c: '))
if(abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < a + b):
    if(a == b and a == c and b == c):
        print('\nVocê criou um triângulo equilátero!\n')
    elif((a == b and a != c) or (b == c and  b != a) or (a == c and a != b)):
        print('\nVocê criou um triângulo isósceles!\n')
    else:
        print('\nVocê criou um triângulo escaleno!\n')
else:
    print('\nOs lados inseridos não formam um triângulo!\n')