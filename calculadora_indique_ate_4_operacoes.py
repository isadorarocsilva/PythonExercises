#Exercício 1.2 da página 75 do livro 
#Elabore um algoritmo que, dados dois vetores inteiros de 20 posições, efetue as respectivas
#operações indicadas por outro vetor de 20 posições de caracteres também fornecido pelo
#usuário, contendo as quatro oerações aritméticas em qualquer combinação e armazenando os
#resultados em um terceiro vetor.
vetor_int_1 = []
vetor_int_2 = []
vetor_char = []
vetor_resp = []
for i in range(3):
    vetor_int_1.append(int(input('Digite o primeiro valor: ')))
    vetor_char.append(input('Digite + ou - ou * ou /: '))
    vetor_int_2.append(int(input('Digite o segundo valor: ')))
    if vetor_char[i] == "+":
        vetor_resp.append(vetor_int_1[i] + vetor_int_2[i])
        print('{}+{}={}'.format(vetor_int_1[i], vetor_int_2[i], vetor_resp[i]))
    elif vetor_char[i] == "-":
        vetor_resp.append(vetor_int_1[i] - vetor_int_2[i])
        print('{}-{}={}'.format(vetor_int_1[i], vetor_int_2[i], vetor_resp[i]))
    elif vetor_char[i] == "*":
        vetor_resp.append(vetor_int_1[i] * vetor_int_2[i])
        print('{}x{}={}'.format(vetor_int_1[i], vetor_int_2[i], vetor_resp[i]))
    elif vetor_char[i] == "/":
        vetor_resp.append(vetor_int_1[i] - vetor_int_2[i])
        print('{}/{}={}'.format(vetor_int_1[i], vetor_int_2[i], vetor_resp[i]))
    else:
        print('Use apenas as operações básicas.\n')