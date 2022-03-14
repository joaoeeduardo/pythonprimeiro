largura = float(input('Qual a largura da parede em metros: '))
altura = float(input('Qual a altura da parede em metros: '))
area = largura * altura
tinta = area / 2 
print('Sua parede tem uma dimensão de {:.2f}x{:.2f}, portanto ela tem {:.2f} m² de aréa.'.format(largura, altura, area))
print(' Com isso será necessário {:.2f} litros de tinta para pintar a parede.'.format(tinta))
