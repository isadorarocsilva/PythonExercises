print('*************************************************************')
print('**************** Jogo da Adivinhação ************************')
print('** Adivinhe um número e vejamos se acerta o número secreto **')
print('*************************************************************')

numero_secreto = 13
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print('Tentativa {} de {}\n'.format(rodada, total_de_tentativas))
    chute = int(input('Digite um número: '))
    print('O seu chute é o número {}\n'.format(chute))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print('Parabéns! Você acertou o número secreto.\n')
        break
    elif(maior):
        print('Você errou! Seu chute foi maior que o número secreto.\n')
    elif(menor):
        print('Você errou! Seu chute foi menor que o número secreto.\n')
    rodada = rodada + 1

print('Fim de Jogo.\n')
