vel = int(input('Digite a velocidade: '))
if vel > 80:
    valor = (vel - 80) * 7
    print('Sua velocidade é de {} km/h e você foi multado! O valor a ser pago é de R${:.2f}'.format(vel, valor))
else:
    print('Sua velocidade é de {} km/h. Boa viagem!'.format(vel))