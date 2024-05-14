from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))

idade = (date.today().year) - ano

if idade < 18:
    tempo = 18 - idade
    alistamento = date.today().year + idade
    print('Ainda é cedo para se alistar. Ainda faltam {} anos para você conseguir se alistar! O seu alistamento será em {}'.format(tempo, alistamento))
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    tempo = idade - 18
    alistamento = date.today().year - tempo
    print('Você tem {} anos e já se passaram {} anos do seu período de alistamento. O seu alistamento foi em {}.'.format(idade, tempo, alistamento))



    
