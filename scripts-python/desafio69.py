qtdCadastro = 0
maior = 0
menor = 0
homens = 0
op = ''
while op != 'N': 
    idade = int(input('Digite a idade :'))
    sexo = str(input('Digite o Sexo. [M/F]')).upper().strip()[0]
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Digite o Sexo. [M/F]')).upper().strip()[0]
    qtdCadastro += 1
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        menor += 1
    op = str(input('Deseja inserir mais pessoas? [S/N]: ')).upper().strip()
    
print(f'{maior} pessoas tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{menor} mulheres tem menos de 20 anos.')
