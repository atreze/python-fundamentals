#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guardar em um dicionário
#No final mostrar em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter

jogos = dict()

for c in range(1,5):
    jogos[f'Jogador_{c}'] = randint(1,6)

for jogador, dado in jogos.items():
    print(f'{jogador} tirou {dado} no dado.')

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

if ranking[0][1] == ranking[1][1]:
    print(f'🤝 HOUVE EMPATE! {ranking[0][0]} e {ranking[1][0]} tiraram {ranking[0][1]}.')
else:
    print(f'🏆 O vencedor foi {ranking[0][0]} com {ranking[0][1]} pontos!')
