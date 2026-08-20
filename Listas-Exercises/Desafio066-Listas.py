#Criar um programa que possa ler vários números, cadastrar em uma lista. Caso o n
#exista, ele não será adicionado. No final serão exibidos todos os n em ordem crescente

numeros = list()
contador = 0

while True:
    print('='*40)
    n = (int(input('Digite o número:')))

    if n not in numeros:
        numeros.append(n)
        print('Número adicionado')
    else:
        print('Valor duplicado, não será adicionado')
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta == 'N':
        break
print('-=' * 20)
numeros.sort()
print(f'Você digitou os valores: {numeros}')
