#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta 
#para graus Fahrenheit.

celcius = float(input('Temperatura: '))
fahrenheit = (celcius * 1.8) + 32
print('\n{:.2f}°C = {:.2f}°F\n'.format(celcius, fahrenheit))