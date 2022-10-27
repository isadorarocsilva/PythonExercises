print('\nOs números entre 1.000 e 2.000 que quando divididos por 11 tem resto 5 são:\n')
for n in range(1000, 2001):
    if n % 11 == 5:
        print('{}\n'.format(n))
