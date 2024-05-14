salario = float(input('Digite o salário: '))
aumento = float(input('Digite a porcentagem de aumento: '))
op1 = aumento/100
op2 = salario * op1
op3 = salario + op2
print('O seu salário com o aumento de {:.0f} por cento é igual á R$ {} reais'.format(aumento, op3)) 