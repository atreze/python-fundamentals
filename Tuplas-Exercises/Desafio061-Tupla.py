#Criar um programa que gere 5 números aleatórios e colocar dentro da tupla.
#Depois, mostrar a listagem de números gerados e também indique o menor e maior valor

from random import randint

numeros = tuple(randint(1, 100) for _ in range(5))

print(f'Listagem de números gerados: {numeros}')
print(f'O maior número gerado é o {max(numeros)}')
print(f'O menor número gerado é o {min(numeros)}')
