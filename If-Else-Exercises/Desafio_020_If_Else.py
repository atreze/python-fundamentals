#Peça para o PC gerar um número aleatório e pergunte esse número ao usuário.
#Veja se ele acerta

import random

numero = random.randint(1,5)
numero_usuario = int(input('Qual foi o número escolhido pelo PC? Digite entre 1 e 5:\n'))

if numero_usuario == numero:
    print('Parabéns, você acertou!!')
else:
    print('Putz, não foi dessa vez!!\n')
print('====FIM====')
