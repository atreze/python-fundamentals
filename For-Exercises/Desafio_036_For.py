#Programa que mostre uma contagem regressiva de 0 a 10 e com pausa de 1 segundo entre eles

import time

for contador in range(10, 0, -1):
    print(contador)
    time.sleep(1)
print('Fim')
