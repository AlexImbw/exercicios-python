peso = float(input('Qual o seu peso ? '))
altura = float(input('Qual a sua altura? '))

imc = peso / (altura*altura)

if imc < 18.5:
    print('Você está ABAIXO do peso!')
elif (imc >= 18.5) and (imc <= 25):
    print('Você está no peso ideal!')
elif (imc > 25) and (imc <= 30):
    print('Você está com SOBREPESO!')
elif (imc > 30) and (imc <= 40):
    print('Você está com OBESIDADE!')
else:
    print('Você está com imc acima de 40 e tem OBESIDADE MORBIDA!')