salario = float(input('Me informe quanto você ganha atualmente R$ '))
aumento = salario * 10 / 100
aumento2 = salario * 15 / 100
salariofinal2 = salario + aumento2
salariofinal = salario + aumento
if salario > 1250:
    print('Ok, você recebendo {:.2f}, a partir de agora seu salario ira aumentar 10%, ficará a partir de agora em {:.2f}.'.format(salario, salariofinal))
else:
    print('Ok, você recebendo {:.2f}, a partir de agora seu sálario ira aumebntar 15%, ficará a partir de agora em {:.2f}.'.format(salario, salariofinal2))    