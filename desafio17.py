from math import hypot
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hi = hypot(co, ca)
print('O cateto oposto mede {}, e o adjacente mede {}, com isso sua jipotenusa é {:.2f}.'.format(co, ca, hi))