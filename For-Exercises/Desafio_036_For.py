##Calcular a soma entre todos os números ímpares que são múltiplos de 3 em um intervalo
#de 0 a 500

s = 0

for contador in range(0, 500, 3):
    if contador % 2 != 0:
        print(contador)
        s += contador
print('A soma dos multiplos entre 0 a 500 são: {}'.format(s))
