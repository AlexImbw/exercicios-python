n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if (n1 + n2) > n3 and (n1 + n3) > n2 and (n2 + n3) > n1:
    input('É possível criar um triângulo com essas medidas!')
else:
    input('Não é possível criar um triângulo com essas medidas!')