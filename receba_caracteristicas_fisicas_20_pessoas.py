qnt_pessoas_anos_quilo = 0
soma_idade = 0
media_idades = 0
percentagem_olho_azul = 0
qnt_pessoas_ruivas_sem_azul = 0

for i in range(1, 21):
    print('\n--------- {}° PESSOA ---------'.format(i))
    idade = int(input('Idade: '))
    peso = float(input('Peso: '))
    altura = float(input('Altura: '))
    cor_olho = str(input('Cor dos olhos [A - Azul, P - Preto, V - Verde e C - Castanho]: '))
    cor_cabelo = str(input('Cor do cabelo [P - Preto, C - Castanho, L - Louro e R - Ruivo]: '))

    if idade > 50 and peso < 60:
        qnt_pessoas_anos_quilo += 1
    
    if altura < 1.50:
        soma_idade += idade
        media_idades = soma_idade / i
    
    if cor_olho == 'A':
        percentagem_olho_azul = (1 * i) / 20 
    
    if cor_cabelo == 'R' and cor_olho != 'A':
        qnt_pessoas_ruivas_sem_azul += 1


print('\nQuantidade de pessoas acima de 50 anos com menos de 60kg: {}'.format(qnt_pessoas_anos_quilo))
print('A média das idades das pessoas com menos de 1,50m: {}'.format(media_idades))
print('A percentagem de pessoas com olho azul é: {:.2f}'.format(percentagem_olho_azul))
print('Quantidade de pessoas ruivas que não tem olhos azuis: {}'.format(qnt_pessoas_ruivas_sem_azul))
