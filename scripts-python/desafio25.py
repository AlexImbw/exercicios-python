nome = input('Digite seu nome: ')
verify = nome.find('Silva')
if verify > -1:
    print('Você tem Silva em alguma parte do seu nome!')
else:
    print('Você não tem Silva em nenhuma parte do seu nome!')