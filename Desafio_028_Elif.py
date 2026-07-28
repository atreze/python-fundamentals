#Leia um número inteiro e peça pra escolher uma opção entre 1 e 3. Mostre na tela
#base de conversão. 1 - binário, 2 - octal, 3- decimal

numero = int(input('Digite um número inteiro: '))

print('Escolha qual será a base de conversão: ')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')

numero2 = int(input('Escolheu: '))

binario = bin(numero)[2:]
octal = oct(numero)[2:]
hexadecimal = hex(numero)[2:].upper()
