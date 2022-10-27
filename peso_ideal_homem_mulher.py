print('\nIndicaremos o seu peso ideal, para isso precisamos do seu sexo (M para masculino, F para feminino)\ne da sua altura em metro (um metro e vinte = 1.20)\n')
sexo = input('Indique o seu sexo: ')
altura = float(input('Indique sua altura: '))

if(sexo == 'M'):
    peso_ideal = (72.7 * altura) - 58
    print('\nSeu peso ideal é {:.1f}.\n'.format(peso_ideal))
elif(sexo == 'F'):
    peso_ideal = (62.1 * altura) - 44.7
    print('\nSeu peso ideal é {:.1f}.\n'.format(peso_ideal))
elif(sexo != 'M' or sexo != 'F'):
    print('\nO dado sobre o sexo está inválido!\n')
    