from random import randint

maior = 0
menor = 0

n1 = randint(0,9)
n2 = randint(0,9)
n3 = randint(0,9)
n4 = randint(0,9)
n5 = randint(0,9)

sorteio = n1, n2, n3, n4, n5
print('='*45)
print(f'Os valores sorteados foram: {sorteio}')
print('='*45)
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')