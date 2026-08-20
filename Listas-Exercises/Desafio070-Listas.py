#Criar um programa que possa digitar 7 valores numéricos, cadastrar em uma lista única.
#Manter separado os números pares e ímpares
#No final mostrar os valores pares e ímpares em ordem crescente.

lista = list()
pares = list()
impares = list()

for c in range(0,7):
    n = int(input('Digite um valor: '))
    lista.append(n)
print(f'A lista original: {lista}')

for contador in lista:
    if contador % 2 == 0:
        pares.append(contador)
pares = sorted(pares)
print(f'Cópia da lista de pares em ordem crescente: {pares}')

for contador2 in lista:
    if contador2 % 2 != 0:
        impares.append(contador2)
impares = sorted(impares)
print(f'Cópia da lista de ímpares em ordem crescente: {impares}')
