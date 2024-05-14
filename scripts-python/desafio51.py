inicio = int(input('Digite o número inicial: '))
passo = int(input('Digite o passo: '))
decimo = inicio + (10 - 1) * passo
cc = int(0)
for c in range(inicio, decimo + passo, passo):
   
    print(c)