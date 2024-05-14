n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if (n1 + n2) > n3 and (n1 + n3) > n2 and (n2 + n3) > n1:
    print('É possível criar um triângulo com essas medidas!')

    if (n1 == n2) and (n1 == n3) and (n2 == n3):
        print('Esse é um triângulo EQUILÁTERO!')
    
    elif n1 != n2 != n3 != n1:
        print('Esse é um triângulo ESCALENO!')

    else:
        print('Esse é um triângulo ISÓSCELES!')
else:
    print('Não é possível criar um triângulo com essas medidas!')

