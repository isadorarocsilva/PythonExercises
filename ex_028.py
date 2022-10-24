#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e 
#peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
#OBS: >>EU<< fiz com número de tentativas, como forma de implementar o exercício.
from random import randint
num_ganhador = randint(0, 5)
vezes = 3
print('Digite um número entre 0 e 5 e veja se acerta a escolha do computador! Você tem até 3 tentativas.\n')
while vezes != 0:
    chute = int(input('Você tem {} tentativas, seu chute: '.format(vezes)))
    if chute < 6 and chute > -1:
        if chute == num_ganhador:
            print('Parabéns! Você acertou!\n')
            break
        else:
            print('Errou! Tente novamente!\n')
    else:
        print('Eu disse números entre 0 e 5! Tente novamente!\n')
    vezes -= 1
print('Fim das tentativas!\n')