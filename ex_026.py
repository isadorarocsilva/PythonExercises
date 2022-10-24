#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A'
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez
frase = input('Insira uma frase: ').strip().upper()
#consciderando os espaços:
primeiro_aparecimento = frase.find('A')
ultimo_aparecimento = frase.rfind('A')
print('A letra a aparece {} vezes.\n'.format(frase.count('A')))
print('A primeira aparição é na {}° posição e a última é na {}° posição, considerando os espaços.\n'.format(primeiro_aparecimento+1, ultimo_aparecimento+1))
#desconsiderando os espaços:
lista_frase = frase.split()
frase_sem_espaços = ''.join(lista_frase)
p_aparecimento = frase_sem_espaços.find('A')
u_aparecimento = frase_sem_espaços.rfind('A')
print('Desconsciderando os espaços, a primeira aparição é na {}° posição e a última é na {}° posição.\n'.format(p_aparecimento+1, u_aparecimento+1))