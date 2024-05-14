n1 = input('Digite o primeiro valor: ')
n2 = input('Digite o segundo valor: ')

if n1 > n2: 
    print('O PRMEIRO número é maior!')
elif n2 > n1:
    print('O SEGUNDO número é maior!')
elif n1 == n2:
    print('Não existe valor maior, {} e {} são iguais!'.format(n1, n2))