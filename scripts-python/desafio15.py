dia = int(input('Quantos dias alugado? '))
kilo = float(input('Quantos km rodados? '))
aluguel = 60
kmrodado = 0.15

valorAluguel = dia * aluguel + kmrodado*kilo

print('O valor a ser pago é R$ {:.2f}'.format(valorAluguel))

