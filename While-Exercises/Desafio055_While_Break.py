#Um programa que jogue par ou impar. O programa é interrompido quando o usuário
#perder. Mostre o total de vitórias consecutivas que ele conseguiu no fim do jogo.

import random

vitoria = 0

print('----------------------JOGO ÍMPAR OU PAR COM A MÁQUINA-------------------------')

while True:
    jogador = int(input('Digite um valor: '))
    computador = random.randint(1, 10)
    print(computador)
    total = jogador + computador

    par_ou_impar = ' '
    while par_ou_impar not in 'PI':
        par_ou_impar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    print(' DEU PAR' if total % 2 == 0 else ' DEU IMPAR')

    if par_ou_impar == 'P':
        if total % 2 == 0:
            print('Você VENCEU! Bora novamente...')
            vitoria += 1
        else:
            print('Você perdeu!!')
            break
    elif par_ou_impar == 'I':
        if total % 2 != 0:
            print('Você VENCEU! Bora novamente...')
            vitoria += 1
        else:
            print('Você perdeu!!!')
            break
print(f'O total de vitórias consecutivas foram {vitoria}')
