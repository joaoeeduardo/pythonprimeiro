preço = float(input('Preço inicial do produto: '))
desconto = preço*5/100
preçofinal = preço - desconto
print('Caro clinte, seu produto no valor de {}, com o desconto de 5%, seu produto saíra a {:.2f}'.format(preço, preçofinal))

