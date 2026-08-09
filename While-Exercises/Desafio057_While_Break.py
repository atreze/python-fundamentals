#Ler preço e nome de vários produtos. Perguntar se deseja continuar. No final mostre:
# a - Total gasto na compra
# b - Quantos custam mais de > 100
# c - Qual o nome do produto mais barato


contador_mais_100 = 0
tot_comprado = 0
mais_barato = 0
mais_barato_nome = ' '
cont = 0

while True:
    nome = str(input('Digite o nome do seu produto: '))
    preco_produto = float(input('Digite o preço do seu produto: '))

    tot_comprado += preco_produto
    cont += 1

    if preco_produto > 100:
        contador_mais_100 += 1

    if cont == 1 or preco_produto < mais_barato:
        mais_barato = preco_produto
        mais_barato_nome = nome

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'O preço total é {tot_comprado:.2f} reais')
print(f'Total dos produtos mais de 100 reais: {contador_mais_100}')
print(f'O produto mais barato é o {mais_barato_nome}, preço {mais_barato:.2f} reais')
