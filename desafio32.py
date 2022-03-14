distancia = float(input('Qual a distancia da sua viagem em km? '))
d200 = distancia * 0.5
d300 = distancia *0.45
if distancia <=200:
    print('Sua viagem será de {:.0f} km, então ficará no valor de {:.2f}.'.format(distancia, d200))
else:
    print('Sua viagem será de {:.0f} km, então ficará no valor de {:.2f}.'.format(distancia, d300))