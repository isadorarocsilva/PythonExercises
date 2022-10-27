c = float(input('Insira o valor do capital: '))
i = float(input('Insira o valor da taxa de empréstimo: '))
n = int(input('Indique o número de períodos: '))

jurosim = c*i*n

print(f'O valor de juros simples a ser pago é de {jurosim} reais.')
