#Desenvolva um programa que pergunte a distância de uma viagem em km. 
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km 
#e R$0,45 para viagens mais longas.
print('\nPREÇOS PASSAGENS!\nConsulte aqui o preço da sua passagem:\n')
km=float(input('Insira a quilometragem da viagem em km: '))
if km <= 200:
    preco_passagem = km * 0.50
else:
    preco_passagem = km * 0.45
print('\nO preço da sua passagem é R${:.2f}.\nVolte sempre!\n'.format(preco_passagem))