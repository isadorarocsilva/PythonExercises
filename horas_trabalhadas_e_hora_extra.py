#Construa um algoritmo que leia as variáveis C e N, respectivamente código e número de horas trabalhadas de um operário. E calcule o salário sabendo-se que ele ganha R$ 10,00 por hora. Quando o número de horas exceder a 50 calcule o excesso de pagamento armazenando-o na variável E, caso contrário zerar tal variável. A hora excedente de trabalho vale R$ 20,00. No final do processamento imprimir o salário total e o salário excedente.
codigo = int(input('Código do operário: '))
horas = int(input('Número de horas trabalhadas: '))
if horas <= 50:
  salario = 10 * horas
else:
  h_excedente = horas - 50
  salario = 10 * (horas - h_excedente)
  salario_excedente = h_excedente * 20
  print('\nO salário extra será de R${:.2f}'.format(salario_excedente))
  
print ('\nO salário do operador será R${:.2f}\n'.format(salario))