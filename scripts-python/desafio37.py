n1 = int(input('Digite um número: '))
print('Ok, você digitou o número {}'.format(n1))
print('''QUAL DAS OPÇÕES VOCÊ DESEJA?:
1 para BINÁRIO
2 para OCTAL
3 para HEXADECIMAL''')
opcao = int(input('DIGITE AQUI: '))

if opcao == 1:
    print(bin(n1)[2:]) #[2:] faz o fatiamento para pegar a partir do segunto item
elif opcao == 2:
    print(oct(n1)[2:])
elif opcao == 3:
    print(hex(n1)[2:])

 
