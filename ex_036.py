#Escreva um programa para aprovar o empréstimo bancário para a 
#compra de uma casa. O programa vai perguntar o valor da casa, 
#o salário do comprador e em quantos anos ele vai pagar. Calcule
#o valor da prestação mensal, sabendo que ela não pode exercer 30% 
#do salário ou então o empréstimo será negado.
valor_casa = float(input('Informe valor da casa: '))
salario = float(input('Informe o seu salário: '))
anos = int(input('Informe, em anos, quanto tempo você pretende pagar: '))
prestacao_mensal = valor_casa / (anos * 12)
if prestacao_mensal > (salario * 0.3):
    print('Empréstimo negado, o valor da prestação excede em 30% do seu salário.')
else:
    print('Sucesso!')