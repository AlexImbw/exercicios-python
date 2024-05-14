import random
from time import sleep
n1 = 0
n2 = 1
n3 = 2
n4 = 3
n5 = 4
n6 = 5
lista = [n1, n2, n3, n4, n5, n6]
escolhido = random.choice(lista)

numero = int(input('Eu acabei de pensar em um numero. Tente adivinhar que número foi esse. Digite aqui: '))
print('PROCESSANDRO...')
sleep(3)
if numero == escolhido:
    print('Parabéns, você adivinhou meu pensamento! Eu pensei em {}'.format(escolhido))
else:
    print('Você errou! Eu pensei no número {}. Tente outra vez!'.format(escolhido))