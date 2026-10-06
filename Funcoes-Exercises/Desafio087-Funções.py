#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
#o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='Desconhecido',gols=0):
    return f'Jogador {nome} fez {gols} gols'

j = str(input('Nome do jogador: ')).strip()
g = str(input(f'Número de gols: ')).strip()

if g.isnumeric():
    gols_feitos = int(g)
else:
    gols_feitos = 0

if j == '':
    print(ficha(gols=gols_feitos))
else:
    print(ficha(j,gols_feitos))
