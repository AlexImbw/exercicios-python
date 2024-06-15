varFinal = ''
ext = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

numero = int(input('Digite um número entre 0 e 20: '))
if numero < 0 or numero > 20:
    while numero < 0 or numero > 20:
        numero  = int(input('Tente novemente. Digite um número entre 0 e 20: '))
varFinal = ext[numero]
print(f'Você digitou o número {varFinal}!')
