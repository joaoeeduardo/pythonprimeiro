m = float(input('Me fale o seu valor inicialmete em metros para que depois eu possa fazer a conversão altomaticamente: '))
km = m / 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
cm = m * 100
mm = m * 1000
print('Seu valor em metros é {}. \n Seu valor em cm é {}. \n Em mm seu valor é {}. \n Seu valor em dm é {}. \n Seu valor em dam é {}. \n Seu valor em hm é {}. \n Seu valor em km é {}'.format(m, cm, mm, dm, dam, hm, km))