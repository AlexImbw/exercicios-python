s = int(0)
num = 0
while True:
    num = int(input('Digite o número desejado: '))
    if num >= 0:
        print('-'*12)
        for c in range(1, 10):
            s = s + 1
            print('{} X {:2} = {}'.format(num, s, num * s))
        print('-'*12)
    else:
        break    
print('PROGRAMA DA TABOADA ENCERRADO. VOLTE SEMPRE!')