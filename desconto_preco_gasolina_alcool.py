litro_comprado = float(input('\nInsira a quantidade de litros comprados: '))
tipo_combustivel = input('Insira o tipo de combustível, A para álcool e G para gasolina: ')

if(tipo_combustivel == 'A'):
    if(litro_comprado <= 20):
        preco_total = litro_comprado * 2.90
        preco_com_desconto = preco_total - (preco_total * 0.03)
        print('\nItem: Álcool, Qnt: {:.1f}L\nValor normal: {:.2f}R$, Valor com desconto: {:.2f}R$.\n'.format(litro_comprado, preco_total, preco_com_desconto))
    else:
        preco_total = litro_comprado * 2.90
        preco_com_desconto = preco_total - (preco_total * 0.05)
        print('\nItem: Álcool, Qnt: {:.1f}L\nValor normal: {:.2f}R$, Valor com desconto: {:.2f}R$.\n'.format(litro_comprado, preco_total, preco_com_desconto))
elif(tipo_combustivel == 'G'):
    if(litro_comprado <= 20):
        preco_total = litro_comprado * 3.30
        preco_com_desconto = preco_total - (preco_total * 0.04)
        print('\nItem: Álcool, Qnt: {:.1f}L\nValor normal: {:.2f}R$, Valor com desconto: {:.2f}R$.\n'.format(litro_comprado, preco_total, preco_com_desconto))
    else:
        preco_total = litro_comprado * 3.30
        preco_com_desconto = preco_total - (preco_total * 0.06)
        print('\nItem: Álcool, Qnt: {:.1f}L\nValor normal: {:.2f}R$, Valor com desconto: {:.2f}R$.\n'.format(litro_comprado, preco_total, preco_com_desconto))
else:
    print('\nTipo de combustível inválido!\n')
