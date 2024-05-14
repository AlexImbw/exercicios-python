n1 = int((input('Digite um numero entre 0 e 9999: ')))
if n1 >= 0 and n1 <= 9999:
    n1 = str(n1)
    print('Unidade: ',n1[3])
    print('Dezena: ',n1[2])
    print('Centena: ',n1[1])
    print('Milhar: ',n1[0])
else:
    print('O número digitado não correponde ao solicitado')