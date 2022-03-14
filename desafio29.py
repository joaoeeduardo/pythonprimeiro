from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vo pensar em um número entre 0 e 5. Tente adivinhar')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
sleep(3)
if jogador == computador:
    print('Você ganhou meus parabéns!')
else:
    print('Ganhei! Eu pensei no número {}, e não no {}!'.format(computador, jogador))
  
