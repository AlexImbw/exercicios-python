cont = int(0)
s = int(0)
for c in range (1, 501):
    if (c % 2 ) == 1 and (c % 3) == 0:
        cont = cont + 1
        s = s + c
print(s)
print('Quantidade de todos os valores somados é {}.'.format(cont))