n1 = int(input('Digite um numero: '))
tot = 0
for c in range(1, n1 +1):
    if n1 % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
if tot == 2:
    print('\n O número {} é primo!'.format(n1))
else:
    print('\n O numero {} não é primo!'.format(n1))
