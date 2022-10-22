#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro 
#custa R$60 por dia e R$0,15 por Km rodado.

km_rodados = float(input('Quantos km já foram rodados?\n'))
dias_alugado = int(input('Quantos dias o carro foi alugado?\n'))

preco_pagamento = (dias_alugado * 60) + (km_rodados * 0.15)
print('Valor do pagamento: {:.2f}.\n'.format(preco_pagamento))