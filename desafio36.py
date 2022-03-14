r1 = float(input('Me informe o tamanho da reta 1: '))
r2 = float(input('Me informe o tamanho da reta 2: '))
r3 = float(input('Me informe o tamanho da reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Portanto essas retas podem formar um triângulo.')
else:
    print('Portanto essas retas não podem formar um triângulo.')    