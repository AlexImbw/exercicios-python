times = 'Flamengo', 'Bahia', 'Bota Fogo', 'Athetico-PR', 'Bragantino', 'São Paulo', 'Palmeiras', 'Cruzeiro', 'Atlético-MG', 'Internacional', 'Fortaleza', 'Juventude', 'Grêmio', 'Vasco da Gama', 'Corinthians', 'Fluminense', 'Criciúma', 'Atlético-GO', 'Cuiabá', 'EC Vitória'
lanterna = 0

lanterna = len(times) - 4

print(times)
print('-='*30)
print('Os 5 primeiros colocados são:')
print(times[0:5])
print('-='*30)
print('Os 4 ultimos colocados são:')
print(times[lanterna:])
print('-='*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*30)