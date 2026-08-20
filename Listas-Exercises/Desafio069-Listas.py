#Faça um programa que leia nome e peso de várias pessoas guardando em uma lista. No final mostre:
#a - Quantas pessoas foram cadastradas
#b - Listagem com as pessoas mais pesadas
#c - Listagem com as pessoas mais leves

cadastro = list()
temporario = list()
maior = menor = 0

print('=-=-=-=-=LISTAGEM DE PESSOAS=-=-=-=-=-')
while True:
    temporario.append(str(input('Digite o nome: ')))
    temporario.append(float(input('Digite o peso: ')))
    print('=-='*5)

    if len(cadastro) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]

    cadastro.append(temporario[:])
    temporario.clear()
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    print('=-=' * 5)
    if resposta == 'N':
        break

print(f'O número de pessoas cadastradas foram {len(cadastro)} pessoas')

for p in cadastro:
    if p[1] == maior:
        print(f'O maior peso foi de {maior}kg. Peso de [{p[0]}]')

for p in cadastro:
    if p[1] == menor:
        print(f'O menor peso foi de {menor}kg. Peso de [{p[0]}]')
