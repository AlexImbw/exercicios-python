from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você quer: '))
seno = sin(radians(an))
print('O ângulo de {}tem o SENO de {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(an, cosseno))
tangente = tan(radians(an))
print('O ângulo de {} tem a tangente de {:.2f}'.format(an, tangente))