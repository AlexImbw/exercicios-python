from random import randint

maior = 0
menor = 0
n1 = 0

for n1 in range(0,5):
    n1 = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))


print('='*45)
print(f'Os valores sorteados foram: {n1}')
print('='*45)

print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')