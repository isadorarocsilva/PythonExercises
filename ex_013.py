#Faça um algoritmo que leia o salário de um funcinário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Valor salário: '))
aumento = salario * 0.15
print('O novo salário é R${:.2f}.\n'.format(salario+aumento))