#Escreva um programa que leia a velocidade de um carro. 
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.
import random
quilometragem = 0
velocidade = 0
km_multa = 0
ligar = input('Ligar carro [S|N]?')
if(ligar == 'S'):
    velocidade = random.randint(1, 100) #impulso inicial do carro
    print('O carro está andando...\n')
    while velocidade > 0:
        velocidade = random.randint(0, 100)
        quilometragem += 1
        if velocidade == 0:
            print('O carro parou, fim da viagem.\nInformações da viagem:\n')
            break
        if velocidade > 80:
            km_multa += 1
    if quilometragem > 0:
        print('O carro andou {}km no total da viagem.\n'.format(quilometragem))
    if km_multa > 0:
        print('Aviso!\nVocê recebeu uma multa de R${:.2f}\nO carro percorreu {}km com velocidade acima do permitido.\n'.format(km_multa*7, km_multa))
else: 
    print('Você não ligou o carro.\n')

#A forma como o professor resolveu:
#velocidade = float(input('Qual é a velocidade do carro? '))
#if velocidade > 80:
#   print('MULTADO! você excedeu o limite permitido que é 80km/h')
#   multa = (velocidade-80) * 7
#   print('Você deve pagar pagar uma multa de R${:.2f}!'.format(multa))
#print('Tenha um bom dia! Dirija com segurança!')