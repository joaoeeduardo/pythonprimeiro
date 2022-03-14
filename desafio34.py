n1 = float(input('Me fale algum número: '))
n2 = float(input('Me fale outro número: '))
n3 = float(input('Me fale outro número: '))

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3            

print('O menor valor digitado foi {:.0f}.'.format(menor))
print('O maior valor digitado foi {:.0f}.'.format(maior))
