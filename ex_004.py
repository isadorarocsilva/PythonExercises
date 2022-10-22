#ENUNCIADO: Faça um programa que leia algo pelo teclado e 
# mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
a = input('Digite qualquer coisa: ')
print('\n')
if a.isnumeric() == True:
    print('É um número\nTipo primitivo do dado: {}\n'.format(type(a))) 
elif a.isalpha() == True:
    if a.isupper() == True:
        print('É uma palavra/letra totalmente em maiúsculo\nTipo primitivo do dado: {}\n'.format(type(a)))
    if a.islower() == True:
        print('É uma palavra/letra totalmente em minúsculo\nTipo primitivo do dado: {}\n'.format(type(a)))
    if a.istitle() == True:
        print('É uma palavra/letra capitalizada\nTipo primitivo do dado: {}\n'.format(type(a)))
    else:
        print('É uma palavra/letra\nTipo primitivo do dado: {}\n'.format(type(a)))
elif a.isalnum() == True:
    print('É uma palavra/letra com número\nTipo primitivo do dado: {}\n'.format(type(a)))
else:
    print('É espaço vazio\nTipo primitivo do dado: {}\n'.format(type(a)))
