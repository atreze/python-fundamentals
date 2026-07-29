#Jogar jokempô

import random

sua_escolha = (str(input('Escolha sua opção: Pedra, Papel ou Tesoura: '))).lower().strip()

aleatorios = ['pedra', 'papel', 'tesoura']
escolha_aleatorio = random.choice(aleatorios)
print('Escolha pela máquina:', escolha_aleatorio.capitalize())
if sua_escolha not in aleatorios:
    print('Opção invalida')
elif sua_escolha == escolha_aleatorio:
    print('Empate!')
elif(
    (sua_escolha == 'pedra' and escolha_aleatorio == 'tesoura') or
    (sua_escolha == "papel" and escolha_aleatorio == "pedra") or
    (sua_escolha == "tesoura" and escolha_aleatorio == "papel")
):
    print('Você ganhou!')
else:
    print('A máquina ganhou!')
