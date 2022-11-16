#Desenvolva uma lógica que leia o peso e altura de uma pesoa, 
#calcule seu IMC e mostre seu status, de acordo com a tabela
#abaixo:
#Abaixo de 18.5: abaixo do peso
#Entre 18.5 e 25: peso ideal
#25 até 30: sobrepeso
#30 até 40: obesidade
#Acima de 40: obesidade mórbida
altura = float(input('Indique sua altura: '))
peso = float(input('Indique seu peso: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está no sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Você está na obesidade.')
else:
    print('Você está na obesidade mórbida.')