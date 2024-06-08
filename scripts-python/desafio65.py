
n = int(input('Digite um número: '))
op = str(input('Quer continuar? [S] para SIM ou [N] p/ NÃO: '))

c = 1
s = n
med = 0
maior = n
menor = n

while op in 'Ss':
    n = int(input('Digite um número: '))
    op = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    c += 1
    s += n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n

med = s / c
print('Você digitou {} números e a média foi {}'.format(c, med))
print('O maior numero foi {} e o menor foi {}'.format(maior, menor))