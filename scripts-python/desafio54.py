from datetime import date
anoatual = date.today().year
maioridade = 0
menoridade = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    if anoatual - ano >= 21:
        maioridade = maioridade + 1
    else:
        menoridade  = menoridade + 1
print('Temos {} pessoas mais velhas e {} pessoas mais novas'.format(maioridade, menoridade))

