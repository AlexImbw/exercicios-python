inicio = int(input('Digite o número inicial: '))
passo = int(input('Digite o passo: '))
pausa = ''
termo = inicio
c = 1
pausa = 10
total  = 0

while pausa != 0:
    total = total + pausa
    while c <=total:
        print('{} -> '.format(termo), end=' ')
        termo = termo + passo
        c = c + 1
    print('PAUSA')
    pausa = int(input('Quantos temos a mais você quer mostrar? '))
print('FIM')
print('O total de progressão final foi de {}'.format(total))