largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print('A parede tem {} m²! Serão necessários {:.0f} litros de tinta para cobrir a área indicada.'.format(area, tinta))
