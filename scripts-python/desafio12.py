preco = float(input('Digite o preço do produto: '))
desc = float(input('Digite o valor do desconto: '))
conDesc = desc/100
operador = preco*conDesc
npreco = preco - operador
print('O preço do produto com {:.0f} por cento de desconto é R$ {:.2f}'.format(desc, npreco))