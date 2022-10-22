#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Valor produto: '))
desconto = preco * 0.05
print('O produto vale R${:.2f}.\nConsiderando o desconto, ele valerá R${:.2f}.\n'.format(preco, preco-desconto))