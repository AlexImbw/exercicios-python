n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = int
while n3 != 5:
    print('-------=====================-------')
    print('')
    
    n3 = int(input('''O QUE VOCÊ DESEJA FAZER COM ESSES DOIS NÚMEROS?  
    DIGITE [1] PARA SOMAR
    DIGITE [2] PARA MULTIPLICAR
    DIGITE [3] PARA MAIOR
    DIGITE [4] PARA DIGITAR NOVOS NÚMEROS
    DIGITE [5] PARA SAIR DO PROGRAMA
    DIGITAR OPÇÃO: '''))

    print('')
    print('-------=====================-------')
    
    if n3 == 1:
        soma = n1 + n2
        print('A soma de {} com {} é {}'.format(n1, n2, soma))

    elif n3 == 2:
        mult = n1 * n2
        print('Ao multiplicar {} por {} o resultado é {}'.format(n1, n2, mult))

    elif n3 == 3:
        if n1 > n2:
            print('O numero {} é maior que o numero {}'.format(n1, n2))
        elif n2 > n1:
            print('O numero {} é maior que o numero {}'.format(n2, n1))
        else:
            print('Os numeros são exatamente iguais!')
    elif n3 == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
print('FIM DO PROGRAMA!')