salario = float(input('Qual o salário antes do aumento; '))
aumento = salario * 15/100
salariofinal= salario + aumento
print('Senhor, seu sálario no valor de R${} terá um aumento de 15%, a partir de agora seu sálario é de {:.2f}'.format(salario, salariofinal))