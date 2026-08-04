#ler um número e mostrar o fatorial

numero_original = int(input('Digite um numero inteiro: '))
resultado = 1
numero = numero_original

while numero > 1:
    resultado *= numero
    numero -= 1
print('O resultado do fatorial de {} é {}'.format(numero_original, resultado))
