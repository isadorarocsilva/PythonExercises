n = int(input('\nDê um valor para n: '))
soma = 0
while n > 0 :
    soma += 1/n
    n = n-1
print('A soma da sequêcia S é {:.1f}'.format(soma))