km = float(input('Qual a velocidade em que o carro passou? '))
valor = (km - 80) * 7
if km <=80:
    print('Voce está dentro do limite da velocidade, pode continuar sem multa.')
else:
    print('Você esta acima do limite de velocidade, você levará uma multa, 7 reais a cada km/h a mais na velocidade.')    
print('Sua multa sera de R$ {:.2f}.'.format(valor))    
