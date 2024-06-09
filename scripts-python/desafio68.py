import random
print('-='*10)
print('JOGO DO PAR OU ÍMPAR')
print('-='*10)

par = 0
impar = 0
soma = 0
vitorias = 0
derrota = 0


computador = random.randint(0, 10)
jogador = int(input('Digite um número: '))
op = str(input('Você quer [P/I] ?: ')).upper().strip()[0]

soma = computador + jogador

if op == 'P' and soma % 2 == 0:
        print('-'*20)
        print('Você Venceu!')
        print('-'*20)
        vitorias += 1
        print(f'Numero do computador: {computador}')

elif op == 'I' and soma % 2 > 0:
        print('-'*20)
        print('Você Venceu!')
        print('-'*20)
        vitorias += 1
        print(f'Numero do computador: {computador}')

        soma = computador + jogador
elif op == 'P' and soma % 2 > 0:
        print('-'*20)
        print('Você perdeu!')
        print('-'*20)
        derrota = 1
        
elif op == 'I' and soma % 2 == 0:
        print('-'*20)
        print('Você Perdeu!')
        print('-'*20)
        derrota = 1

while derrota != 1:

    computador = random.randint(1, 10)
    jogador = int(input('Vamos jogar novamente!: '))
    op = str(input('Você quer [P/I] ?: ')).upper().strip()

    soma = computador + jogador

    if op == 'P' and soma % 2 == 0:
        print('-'*20)
        print('Você Venceu!')
        print('-'*20)
        vitorias += 1
        print(f'Numero do computador: {computador}')

    elif op == 'I' and soma % 2 > 0:
        print('-'*20)
        print('Você Venceu!')
        print('-'*20)
        vitorias += 1
        print(f'Numero do computador: {computador}')

        soma = computador + jogador
    elif op == 'P' and soma % 2 > 0:
        print('-'*20)
        print('Você perdeu!')
        print('-'*20)
        derrota = 1
        
    elif op == 'I' and soma % 2 == 0:
        print('-'*20)
        print('Você Perdeu!')
        print('-'*20)
        derrota = 1
print('-'*20)
print(f'Total de vitórias: {vitorias}.')
print('-'*20)
print(f'Numero do computador: {computador}.')


