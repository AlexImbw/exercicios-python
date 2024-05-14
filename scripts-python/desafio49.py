s = int(0)
num = int(input('Digite o número desejado: '))
print('-'*12)
for c in range(1, 10):
    s = s + 1
    print('{} X {:2} = {}'.format(num, s, num * s))

print('-'*12)