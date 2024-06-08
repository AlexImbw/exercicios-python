n = int(input('Digite um número: '))
c = 0
s = 0
while n != 999:
    c += 1
    s = s + n
    n = int(input('Digite outro número: '))
print('FIM')
print('Você digitou {} numero(s)'.format(c))
print('O total da soma entre esses números é {}'.format(s))