n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print('{} é o maior entre os três números digitados!'.format(n1))
else:
    if n2 > n1 and n2 > n3:
        print('{} é o maior entre os três números digitados!'.format(n2))
    else:
        print('{} é o maior entre os três números digitados!'.format(n3))

if n1 < n2 and n1 < n3:
    print('{} é o menor entre os três números digitados!'.format(n1))
else:
    if n2 < n1 and n2 < n3:
        print('{} é o menor entre os três números digitados!'.format(n2))
    else:
        print('{} é o menor entre os três números digitados!'.format(n3))
    