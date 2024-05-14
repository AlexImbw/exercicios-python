from time import sleep
valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos pretende pagar? '))
print('PROCESSANDO...')
sleep(4)
parcela  = valor / (anos * 12)

if parcela > (salario * 30) / 100:
    print('Infelizmente o seu emprestimo o não foi aprovado!')
else:
    print('Parabens, emprestimo aprovado!')