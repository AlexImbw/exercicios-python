''' inicio = int(input('Digite o número inicial: '))
passo = int(input('Digite o passo: '))
decimo = inicio + (10 - 1) * passo
cc = int(0)
for c in range(inicio, decimo + passo, passo):
    print(c) '''


inicio = int(input('Digite o número inicial: '))
passo = int(input('Digite o passo: '))
pausa = ''
termo = inicio
c = 1

while pausa != 0:
    while c <=10:
        print('{} -> '.format(termo), end=' ')
        termo = termo + passo
        c = c + 1
    print('PAUSA')
    pausa = int(input('Quandos termos a mais você quer mostrar? '))
    while c <= pausa:
        print('{} -> '.format(termo), end=' ')
        termo = termo + passo
        c = c + 1



