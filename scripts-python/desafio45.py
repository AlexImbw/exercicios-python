from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)
print('''Suas opções:
      [ 0 ] Pedra
      [ 1 ] Papel
      [ 2 ] Tesoura''')
jogador = int(input('Faça sua Jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=' *11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' *11)

if computador == 0: #computador jogar pedra
    if jogador == 0:
        print ('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print ('JOGADA INVÁLIDA')
elif computador == 1: # computador jogar papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print ('JOGADA INVÁLIDA')
        
elif computador == 2: # computador jogar tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print ('JOGADA INVÁLIDA')