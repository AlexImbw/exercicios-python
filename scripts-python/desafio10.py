real = float(input('Digite quanto em real você tem: R$'))
dolar = float(3.27)
tot = real/dolar
if real > 1:
    print('Com R$ {:.2f} reais você consegue comprar $ {:.2f} dolares'.format(real,tot))
else:
    print('Com R$ {:.2f} real você consegue comprar $ {:.2f} dolar'.format(real,tot))

