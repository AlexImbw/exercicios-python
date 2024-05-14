from datetime import date
ano = int(input('Qual a sua idade? '))

cat = date.today().year - ano

if cat <= 9:
    print('Você tem {} anos e está na categoria MIRIM!'.format(cat))
elif (cat > 9) and (cat <= 14):
    print('Você tem {} anos e está na categoria INFANTIL'.format(cat))
elif (cat > 14) and (cat <= 19):
    print('Você tem {} anos e está na categoria JUNIOR!'.format(cat))
elif (cat == 20):
    print('Você tem {} anos e está na categoria SÊNIOR!'.format(cat))
else:
    print('Você tem mais de 20 anos e está na categoria MASTER!')