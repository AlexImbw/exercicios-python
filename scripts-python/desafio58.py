import random
from time import sleep
cont = 1
n1 = 0
n2 = 1
n3 = 2
n4 = 3
n5 = 4
n6 = 5
n7 = 6
n8 = 7
n9 = 8
n10 = 9
n11 = 10
lista = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
computador = random.choice(lista)

jogador = int(input('Eu acabei de pensar em um numero. Tente adivinhar que número foi esse. Digite aqui: '))
print('PROCESSANDRO...')
sleep(3)

if jogador == computador:
    print('Parabéns, você adivinhou meu pensamento! Eu pensei exatamente no numero {}'.format(computador))
else:
    while jogador != computador:
        cont = cont + 1
        jogador = int(input('Errou, tente outra vez: '))
        if jogador == computador:
            print('Parabéns, você adivinhou, porém precisouy de {} tentativas.'.format(cont))
