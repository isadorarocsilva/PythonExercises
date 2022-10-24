#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para salários inferiores ou iguais, o aumento é de 15%.
salario = float(input('Quanto é o seu salário em R$? '))
if salario > 1250:
    salario += salario*0.1
    print('\nSeu novo salário será R${:.2f}.\n'.format(salario))
else:
    salario += salario*0.15
    print('\nSeu novo salário é R${:.2f}.\n'.format(salario))