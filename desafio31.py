n = int(input('Me fale o numero que deseja saber se ele é par ou impar: '))
resultador = n % 2
if resultador == 0:
    print('O número {} é PAR.'.format(n))
else:
    print('O número {} é IMPAR.'.format(n))