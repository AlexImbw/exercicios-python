import random
print('-='*10)
print('JOGO DO PAR OU ÍMPAR')
print('-='*10)

par = 0
impar = 0
soma = 0
vitorias = 0

computador = random.randint(1, 10)
jogador = int(input('Digite um número: '))
op = str(input('Você quer [P/I] ?: ')).upper().strip()

soma = computador + jogador

while True:

    if op == 'P' and soma % 2 == 0:
        print('Você Venceu!')
        vitorias += 1
    elif op == 'I' and soma % 2 > 0:
        print('Você Venceu!')
        vitorias += 1
        
        computador = random.randint(1, 10)
        jogador = int(input('Digite um número: '))
        op = str(input('Você quer [P/I] ?: ')).upper().strip()

        soma = computador + jogador
    elif op == 'P' and soma % 2 > 0:
        print('Você perdeu!')
        
    elif op == 'I' and soma % 2 == 0:
        print('Você Perdeu!')

print('-'*20)
print(f'Total de vitórias: {vitorias}.')
print('-'*20)


