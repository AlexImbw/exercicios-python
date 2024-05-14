n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

resultado = (n1+n2) / 2

if resultado >= 7.0:
    print('PARABÉNS!! Você foi aprovado com média {} !'.format(resultado))
elif (resultado > 5.0) and (resultado <= 6.9):
    print('Sua nota é {:.2f} e você está de RECUPERAÇÃO!'.format(resultado))
else:
    print('Sua nota é {:.2f} e você está REPROVADO!'.format(resultado))