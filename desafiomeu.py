p = float(input('Preço original do produto: R$ '))
av = p - (p*10/100)
par = p + (p*10/100)
print('Caso deseje pagar a vista, você terá um desconto de 10% que ficará em R$ {:.2f}, caso queira parcelar, o valor do produto terá um acrescímo de 10%, que ficará em R$ {:.2f}'.format(av, par))
print('Vaor das parcelas caso opte por esse modo de pagamento: ')
print('Dividir em 2x {:.2f} / 2 = {:.2f}'.format(par, par/2))
print('Dividir em 3x {:.2f} / 3 = {:.2f}'.format(par, par/3))
print('Dividir em 4x {:.2f} / 4 = {:.2f}'.format(par, par/4))
print('Dividir em 5x {:.2f} / 5 = {:.2f}'.format(par, par/5)) 
print('Dividir em 6x {:.2f} / 6 = {:.2f}'.format(par, par/6)) 
print('Dividir em 7x {:.2f} / 7 = {:.2f}'.format(par, par/7))
print('Dividir em 8x {:.2f} / 8 = {:.2f}'.format(par, par/8))
print('Dividir em 9x {:.2f} / 9 = {:.2f}'.format(par, par/9))
print('Dividir em 10x {:.2f} / 10 = {:.2f}'.format(par, par/10))
