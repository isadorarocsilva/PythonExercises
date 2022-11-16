#Faça um programa que leia o ano de nascimento de um jovem
#e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar.
#Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou 
#que passou do prazo.
from datetime import date
ano_nascimento = int(input('Digite o ano que você nasceu: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade == 18:
    print('Você está na idade ideal para se alistar.')
elif idade > 18:
    anos_passados = idade - 18
    print('Faz {} anos que você passou do tempo para se alistar.'.format(anos_passados))
else:
    anos_faltando = 18 - idade
    print('Você ainda não chegou na idade ideal, volte em {} anos'.format(anos_faltando))