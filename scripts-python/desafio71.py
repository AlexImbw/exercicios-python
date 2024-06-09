print('-='*20)
print('CAIXA ELETRÔNICO')
print('-='*20)

notas50 = 0
notas20 = 0
notas10 = 0
notas1 = 0

print('-'*40)
valor = int(input('Digite o valor que deseja sacar:' ))
print('-'*40)
while valor >= 50:
    notas50 += 1
    valor -= 50
print(f'Você vai receber {notas50} notas de R$ 50.00')

while valor >= 20:
    notas20 += 1
    valor -= 20
print(f'Você vai receber {notas20} notas de R$ 20.00')

while valor >= 10:
    notas10 += 1
    valor -= 10
print(f'Você vai receber {notas10} notas de R$ 10.00')

while valor >= 1:
    notas1 += 1
    valor -= 1
print(f'Você vai receber {notas1} notas de R$ 1.00')

print('-=' *20)