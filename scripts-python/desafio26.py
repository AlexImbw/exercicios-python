frase = input('Digite qualquer frase: ')
cont0 = frase.count('A')
cont1 = frase.count('a')
contGeral = cont0 + cont1
print('Existem {} letra A nessa frase!'.format(contGeral))
print('A primeira letra A está localizada na posição ',frase.find('A'))

#rfind procura a parti da ultima
