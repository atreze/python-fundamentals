# DESAFIO 093
#
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()

print('=-=-=-=-=APROVEITAMENTO DE JOGADOR=-==-=-=-=-=')
print('=-'*23)
jogador['Nome'] = str(input('Digite o seu nome: ')).strip()
jogador['Partidas'] = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))

jogador['gols'] = []

for c in range(1, jogador['Partidas'] + 1):
    gols.append(int(input(f'Número de gols da partida {c}:  ')))
    jogador['gols'] = gols

jogador['total'] = sum(jogador['gols'])

print('=-' * 20)
print(jogador)

print('=-' * 20)
for i, v in enumerate(jogador['gols'], start=1):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Total de {jogador["total"]} durante o campeonato.')
