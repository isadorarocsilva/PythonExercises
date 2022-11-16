#Elabore um programa que calcule o valor a ser pago por um 
#produto, considerando o seu preço normal e condição de 
#pagamento:
#À vista dinheiro/cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#Em 3x ou mais no cartão: 20% de juros
valor_produto = float(input('Valor do produto: '))
print('[1] À vista em dinheiro ou cheque')
print('[2] À vista no cartão')
print('[3] No cartão, em 2x')
print('[4] No cartão, em 3x ou mais')
cond_pagamento = input('Opção de pagamento: ')
if cond_pagamento == '1':
    preco_desconto = valor_produto * 0.1
    print('Valor total com desconto: R${:.2f}'.format(valor_produto - preco_desconto))
elif cond_pagamento == '2':
    preco_desconto = valor_produto * 0.05
    print('Valor total com desconto: R${:.2f}'.format(valor_produto - preco_desconto))
elif cond_pagamento == '3':
    parcela = valor_produto / 2
    print('Pagamento em 2x de R${:.2f}'.format(parcela))
    print('Valor total: R${:.2f}'.format(valor_produto))
elif cond_pagamento == '4':
    num_parcela = int(input('Quantas parcelas? '))
    valor_total = valor_produto + (valor_produto * 0.2)
    valor_parcela = valor_total / num_parcela
    print('Pagamento em {}x de R${:.2f}.\nValor total do pagamento com juros: R${:.2f}'.format(num_parcela,valor_parcela,valor_total))
else:
    print('ERRO')