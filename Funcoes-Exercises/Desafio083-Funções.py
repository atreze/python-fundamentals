#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    print('-=' * 20)
    print('Analisando os valores passados...')

    if len(num) == 0:
        print('Nenhum valor foi informado.')
        return

    maior_valor = max(num)

    for valor in num:
        print(f'{valor}', end=' ')
    print()

    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior_valor}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior()
