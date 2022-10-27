idades = []
maiores_de_idade = 0

for i in range(10):
    idades.append(int(input('\nDigite idade: ')))

for x in idades:
    if x >= 18:
        maiores_de_idade += 1

print('\nQuantidade de maiores de idade é {}\n'.format(maiores_de_idade))
