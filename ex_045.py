#Crie um programa que faça o comptador jogar Jokenpô com você.
import random
jokepo = ['Pedra', 'Papel', 'Tesoura']
ia = random.choice(jokepo)
print('Escolha: Pedra, Papel ou Tesoura')
humano = input()
if (humano == 'Pedra' and ia == 'Pedra') or (humano == 'Papel' and ia == 'Papel') or (humano == 'Tesoura' and ia == 'Tesoura'):
    print('IA JOGOU {}'.format(ia))
    print('EMPATE')
elif (humano == 'Pedra' and ia == 'Tesoura') or (humano == 'Papel' and ia == 'Pedra') or (humano == 'Tesoura' and ia == 'Papel'):
    print('IA JOGOU {}'.format(ia))
    print('VOCÊ GANHOU!')
else:
    print('IA JOGOU {}'.format(ia))
    print('VOCÊ PERDEU!')