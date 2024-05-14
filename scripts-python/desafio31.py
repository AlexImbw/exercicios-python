dist = float(input('Digite a distância da viagem em Km: '))

if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45

print('O valor a ser pago é de {}'.format(preco))
