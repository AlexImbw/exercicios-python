
s = int(0)
opcao = int(0)
for c in range(1, 7):
    opcao = int(input('Digite um número: '))
    if (opcao % 2) == 0:
        s = s + opcao
print(s)
    