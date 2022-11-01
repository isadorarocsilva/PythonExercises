#Agora usando listas, indique como um troco deve ser dado utilizando-se um número mínimo de 
#notas. Seu algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado 
#desprezando os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 
#reais, e que nenhuma delas esteja em falta no caixa

notas_troco = []
valor_total_compra = float(input('Valor da compra: '))
valor_recebido = float(input('Valor recebido do cliente: '))
valor_troco = valor_recebido - valor_total_compra
cedula = 50 #inicialmente trabalhamos com a maior nota disponível
total_de_cedulas = 0

if valor_total_compra < valor_recebido:
    print('\nTotal do troco é R${:.2f}'.format(valor_troco)) #o exercício não pede, mas coloquei para ter noção nos centávos
    while True:
        if valor_troco >= cedula:
            valor_troco -= cedula
            total_de_cedulas += 1
        else:
            if total_de_cedulas > 0:
                print(f'O troco será composto de {total_de_cedulas} notas de R${cedula}')
            if cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 5
            elif cedula == 5:
                cedula = 2
            elif cedula == 2:
                cedula = 1
            total_de_cedulas = 0
            if valor_troco == 0:
                break
else:
    print('Valor insuficiente para a compra!\n')