print('\nVamos montar um retângulo!!')
a = float(input('Indique uma medida para a largura: '))
b = float(input('Indique uma medida para o comprimento: '))

area = a * b
perimetro = (2 * a) + (2 * b)

print('\nA área do seu retângulo é de {:.0f} e o perímetro é de {:.0f}.'.format(area, perimetro))
