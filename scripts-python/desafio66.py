cont = 0
soma = 0
while True:
    n = int(input('Digite um número ou 999 para Sair: '))
    if n != 999:
        cont = cont + 1
        soma = soma + n
    else:
        break
print(f'Você digitou {cont} e a soma entre eles é igual a {soma}.')
