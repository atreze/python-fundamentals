#Desafio Aula 004, ler um número inteiro e mostrar sua porção inteira

import math

n = float(input('Digite um numero inteiro: '))
print('Sua porção inteira é {}'.format(math.trunc(n)))
