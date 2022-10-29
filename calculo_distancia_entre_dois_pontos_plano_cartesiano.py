#Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer 
#do plano, P(x,y)  e Q(x,y), imprima o resultado do cálculo da distância 
#entre eles.

p = []
q = []
p.append(float(input('Valor para x em P(x,y):')))
p.append(float(input('Valor para y em P(x,y):')))
q.append(float(input('Valor para x em Q(x,y):')))
q.append(float(input('Valor para y em Q(x,y):')))
dist_soma = ((p[0]-q[0])**2 + (p[1]-q[1])**2)
distancia= pow(dist_soma, 0.5)
print('{:.5f}'.format(distancia))

#verificar se resultado bate