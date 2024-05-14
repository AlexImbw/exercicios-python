'''n1 = int(input('DIGITE UM NÚMERO: '))
c = n1
fatorial = 1
while c > 0:
    print(c, end=' '.format(n1))
    print(' X ' if c > 1 else ' = ', end=' ')
    fatorial = fatorial * c
    c = c - 1
print(fatorial) '''

n1 = int(input('DIGITE UM NÚMERO: '))
f = 1
print('O !{} é: '.format(n1))
for c in range(n1, 0, -1):
    print(c, end=' ')
    print(' X ' if c > 1 else ' = ', end=' ')
    f = f * c
    c = c - 1
print('O fatorial é {}'.format(f))