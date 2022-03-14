import random
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('NOme do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))
#ou
from random import choice
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quator aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi o {}.'.format(escolhido))