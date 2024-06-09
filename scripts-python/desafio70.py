print('-'*25)
print('SCRIPT DE VENDAS LOJA')
print('-'*25)

total = 0
caros = 0
cheap = ''
contExpen = 0
op = ''

nomeProduto = str(input('Nome do Produto: '))
precoProduto = float(input('Preço do Produto: R$'))

expensive = precoProduto

op = str(input('Quer continuar? [S/N]: ')).upper().strip()
print('-='*20)

while op != 'N':
    nomeProduto = str(input('Nome do Produto: '))
    precoProduto = float(input('Preço do Produto: R$'))

    total += precoProduto

    if precoProduto > 1000:
        contExpen += 1

    if precoProduto < expensive:
        expensive = precoProduto
        cheap = nomeProduto
    op = str(input('Quer continuar? [S/N]: ')).upper().strip()
    print('-='*20)
    while op != 'S' and op != 'N':
        op = str(input('Quer continuar? [S/N]: ')).upper().strip()
        print('-='*20)

print(f'O valor total da sua compra foi de R${total}.')
print(f'{contExpen} produtos custam mais que R$1.000,00 reais.')
print(f'O produto mais barato na sua compra foi {cheap} custando {expensive}.')