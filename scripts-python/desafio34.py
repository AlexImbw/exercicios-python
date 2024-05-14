salario = float(input('Digite o valor do salário R$: '))

if (salario > 1.250):
    reajuste = salario + (salario * 0.10)
else:
    reajuste = salario + (salario * 0.15)

print ('O seu salário atual é de R${:.2f} reais e com reajuste você vai passar a receber R${:.2f}'.format(salario, reajuste))