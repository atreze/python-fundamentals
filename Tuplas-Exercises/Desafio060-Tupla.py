#Criar tupla com os 20 primeiros do campeonato brasileiro, depois:
# a - Apenas os 5 primeiros colocados
# b - Os últimos 4 colocados
# c - Lista em ordem alfabética
# d - Em que posição está o Corinthians

tabela_brasileirao = (
    'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Botafogo',
    'Ceará', 'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense',
    'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Mirassol',
    'Palmeiras', 'Red Bull Bragantino', 'Santos', 'São Paulo', 'Vasco da Gama'
)

print(f'Os primeiros 5 colocados são {tabela_brasileirao[0:5]}')
print(f'Os últimos colocados são {tabela_brasileirao[-4:]}')
print(sorted(tabela_brasileirao))
print(f'A posição do Corinthians na tabela é {tabela_brasileirao.index('Corinthians') + 1}°')
