#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares 
#ela pode comprar, considere 1 dólar = 3,27 reais.

carteira = float(input('Digite valor na sua carteira: '))
dolares = carteira / 3.27
print('Você pode comprar {:.2f} dólares.\n'.format(dolares))