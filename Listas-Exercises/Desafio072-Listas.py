#Faça um programa que ajude um jogador da Mega Sena a criar palpites.
#Vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 50 para
#cada jogo, cadastrando em uma lista composta.

jogos = []

import random

numero_vezes = (int(input('Quantos vezes deseja jogar? ')))
for c in range(0, numero_vezes):
    palpite = random.sample(range(1, 51), 6)
    palpite.sort()
    jogos.append(palpite)

print('-=' * 15)
print(f'     SORTEANDO {numero_vezes} JOGOS   ')
print('-=' * 15)

for i, jogo in enumerate(jogos):
    print(f'Jogo {i+1}: {jogo}')
