
media_idade = int(0)
mulher_menor = 0
homem_velho = 0
nhmaisvelho = ''
idade = 0
nome = ""
sexo = ""

for c in range(0,4):
    c = c + 1
    print('-----{}º PESSOA -----'.format(c))
    nome = input('NOME: ')
    idade = int(input('IDADE: '))
    sexo = input('SEXO [M/F]: ')
    print('Homem mais velho: {}'.format(homem_velho))

    media_idade = media_idade + idade

    if sexo in 'Mm' and idade > homem_velho:
        homem_velho = idade
        nhmaisvelho = nome
    elif sexo in 'Ff' and idade < 20:
        mulher_menor = mulher_menor + 1

print('A média de idade do grupo é {} anos'.format(media_idade / 4))
if homem_velho == 0:
    print('Não existem homens na lista indicada!')
else:
    print('O homem mais velho se chama {} e ele tem {} anos '.format(nhmaisvelho ,homem_velho))

if mulher_menor == 0:
    print('Não eciste mulheres na lista indicada')    
else:
    print('{} mulheres são menores de idade.'. format(mulher_menor))