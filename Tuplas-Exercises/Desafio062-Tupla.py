#Ler quatro números pelo teclado e guarde-os em uma tupla. No final mostre:
# a - Quantas vezes aparece o número 9
# b - Em que posição foi digitado o primeiro valor 3
# c - Quais foram os números pares

numeros = tuple(int(input('Digite um número inteiro: ')) for _ in range(4))

print(f'O número 9 apareceu {numeros.count(9)} vez')

if 3 in numeros:
    print(f'O número três aparece a primeira vez na posição: {numeros.index(3,0)+1}°')
else:
    print('O número três não foi digitado!')

cont_pares = 0
for n in numeros:
    if n % 2 == 0:
        cont_pares += 1
print(f'O número de números pares é {cont_pares}')
