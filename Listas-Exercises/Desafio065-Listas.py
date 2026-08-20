#Ler 5 números e guardar em uma lista. Mostrar no final qual foi o maior e menor
#e suas respectivas posições

numeros = list()

for cont in range(0,5):
    numeros.append(int(input('Digite o número {cont}:')))

maior = max(numeros)
menor = min(numeros)

print('-=' * 20)
print(f'Você digitou os valores: {numeros}')

print(f'O maior valor foi o {maior}, na posicação {numeros.index(maior)}')
print(f'O menor valor foi o {menor}, na posição {numeros.index(menor)}')
