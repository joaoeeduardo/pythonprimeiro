import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}.'.format(num, math.floor(raiz)))

#ou
from math import sqrt, floor, pow, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}.'.format(num, floor(raiz)))