preco = float(input('Digite o valor do produto R$: '))


print('''Selecione uma das opções de pagamento:
1 - A VISTA NO DINHEIRO COM 10% DE DESCONTO.
2 - A VISTA NO CARTÃO COM 5% DE DESCONTO.
3 - EM ATÉ 2X SEM JUROS NO CARTÃO')
4 - 3X OU MAIS COM ACRESCIMO DE 20% DE JUROS.''')

opcao = int(input('>>> '))

if opcao == 1:
    preco = preco - (preco*0.10)
    print('Pagando a vista no dinheiro o valor final do produto fica em R$ {}'.format(preco))
elif opcao == 2:
    preco = preco - (preco*0.05)
    print('Pagando a vista no cartão o preço do produto vai para R$ {} com 5% de desconto.'.format(preco))
elif opcao == 3:
    print('Em {}x vezes no cartão o produto sai pelo preço normal.'.format(preco))
elif opcao == 4:
    x = float(input('Quantas vezes? '))
    preco = preco + (preco*0.20)
    parcela = preco / x
    print('Em {:.0f}x no cartão o valor da parcela é de {} e o preço do produto é de {} com 20% de Juros. '.format(x, parcela, preco)) 