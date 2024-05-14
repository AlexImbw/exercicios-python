from math import sqrt
a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjacente: '))
c = sqrt(a**2 + b**2)

print('O valor da hipotenusa é {}'.format(c))