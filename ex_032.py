#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
print('\nANOS BISSEXTOS, CONFIRA:\n')
ano_atual = int(input('Quer saber se o ano atual é bissexto [0=Sim|1=Não, quero saber outro ano]? '))
if ano_atual == 0:
    ano_atual = date.today().year
    if ano_atual % 4 == 0 and ano_atual % 100 != 0 or ano_atual % 400 == 0:
        print('\nO ano atual é bissexto.\n')
    else:
        print('\nO ano atual não é bissexto.\n')
else:
    ano = int(input('Qual ano você deseja consultar? '))
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('\nO ano é bissexto.\n')
    else:
        print('\nO ano não é bissexto.\n')