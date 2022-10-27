print('\nA fórmula de Bhaskara é ax^2+bx+c=0, sendo a, b e c os números dados e x a variável a ser encontrada,')
print('neste exercício, nos será dado os valores de a, b e c, e devolveremos as raízes x1 e x2 da equação.\n')

a = float(input('Indique um valor para a: '))
if(a > 0):
    b = float(input('Indique um valor para b: '))
    c = float(input('Indique um valor para c: '))
    print('\nSua equação é {:.1f}x^2+{:.1f}x+{:.1f}=0'.format(a, b, c))

    delta = (b**2) - (4 * a * c)

    if(delta > 0):
        x1 = (- b - pow(delta, 0.5)) / 2 * a
        x2 = (- b + pow(delta, 0.5)) / 2 * a
        print('\nAs raízes são {:.1f} e {:.1f}\n'.format(x1, x2))
    else:
        print('\nO delta é negativo, portanto não há solução para essa equação.')
else:
    print('O valor de a é inválido!')
