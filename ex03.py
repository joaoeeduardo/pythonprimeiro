n1 = int(input('Algum valor: '))
n2 = int(input('Outro Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto {} e a divisão e {:.3f}'.format(s, m, d), end='. ')
print('A Divisão inteira {} e potência {}'.format(di, e))