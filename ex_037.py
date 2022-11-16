#Escreva um programa que leia um número inteiro qualquer
#e peça para o usuário escolher qual será a base de conversão:
#1para binário
#2 para octal
#3 para hexadecimal
decimal = int(input('Digite um número decimal: '))
print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')
converta = input('Digite a opção que deseja converter: ') 
if converta == '1':
    binario =  ''
    while decimal > 0:
        binario += str(decimal%2)
        decimal //= 2
    print('Em binário:')
    print(binario[::-1])
elif converta == '2':
    octal =  ''
    while decimal > 0:
        octal += str(decimal%8)
        decimal //= 8
    print('Em octal:')
    print(octal[::-1])
elif converta == '3':
    hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    r = []
    while decimal > 0:
        r.append(hex[(decimal % 16)])
        decimal //= 16
    print('Em hexadecimal:')
    for i in range(len(r)-1,-1,-1):
        print(r[i],end="")
else:
    print('Opção inválida!')

#Segunda opção:
#if converta == '1':
#    print('Em binário: {}'.format(bin(decimal)))
#elif converta == '2':
#   print('Em octal: {}'.format(oct(decimal)))
#elif converta == '3':
#   print('Em hexadecimal: {}'.format(hex(decimal)))
#else:
#    print('Opção inválida!')
