#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar()
#- A primeira função vai sortear 5 números e vai colocá-los dentro da lista.
#- A segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint

numeros = []

print(f'Sorteando números:', end=' ')
def sorteia():
    for c in range(0, 5):
        num = randint(1, 10)
        numeros.append(num)
        print(f'{num},', end=' ')
    print('... Finalizado!')
    print(f'A lista completa é {numeros}')

def somarPares():
    s = 0
    for c in numeros:
        if c % 2 == 0:
            s += c
    print(f'Somando todos os valores pares, o total é de {s}')

sorteia()
somarPares()
