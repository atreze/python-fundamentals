#Crie um programa que leia vários números e coloque em uma lista.
# a - Quantos números foram digitados
# b - Lista de valores, ordenada de forma decrescente
# c - Se o valor 5 foi digitado e está ou não na lista

numeros = list()
contador = 0

while True:
    print('-' * 20)
    n = int(input('Digite um número: '))
    numeros.append(n)
    contador += 1

    resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta == 'N':
        break

print('-=' * 20)
print(f'Nesta lista foram digitados {len(numeros)} números')
print('-=' * 20)
numeros.sort(reverse=True)
print(f'A lista em ordem decrescente {numeros}')
print('-=' * 20)
qtd = numeros.count(5)
print(f'O número 5 aparece {qtd} vezes na lista')
if 5 in numeros:
    print('O valor 5 apareceu na lista')
