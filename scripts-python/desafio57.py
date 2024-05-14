sexo = str('')
sexo = str(input('Digite seu sexo. [M/F]: '))
while sexo != 'F' and sexo != 'M':
    print('Opção inválida, tente novamemente!')
    sexo = str(input('Digite seu sexo. [M/F]: '))

if sexo == 'F':
    print('Seu sexo é FEMININO!')
else:
    print('Seu sexo é MASCULINO!')
