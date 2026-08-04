#Faça o computador pensar em um número de 0 a 10. Tente adivinhar até acertar.
# Mostrar no final quantos palpites foram necessários para vencer.

from random import randint

n = 0
seu_numero = 0
numero_aleatorio = randint(0,10)

while seu_numero != numero_aleatorio:
    seu_numero = int(input('Digite um numero inteiro: '))
    n += 1
    if seu_numero == numero_aleatorio:
        print('Você acertou o numero aleatorio')
    else:
        print('Ainda não acertou, tente novamente')

print('Foram necessárias {} tentativas para acertar'.format(n))
