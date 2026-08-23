# DESAFIO 094
# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

lista_cadastro = list()
dicionario_cadastro = dict()
idade = []

while True:
    dicionario_cadastro.clear()
    dicionario_cadastro['Nome'] = str(input('Digite seu nome: '))
    dicionario_cadastro['Sexo'] = str(input('Digite seu sexo: ')).upper()[0]
    dicionario_cadastro['Idade'] = int(input('Digite sua idade: '))

    idade.append(dicionario_cadastro['Idade'])
    lista_cadastro.append(dicionario_cadastro.copy())
    print('-=' * 20)
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

media_idade = sum(idade) / len(lista_cadastro)

print('-=' * 25)
print(f'A) Ao todo, temos {len(lista_cadastro)} pessoas cadastradas.')
print(f'B) A média de idade é de {media_idade:.2f} anos.')

print('C) As mulheres cadastradas foram: ', end='')
for p in lista_cadastro:
    if p['Sexo'] == 'F':
        print(f'[{p["Nome"]}] ', end='')
print()

print('D) Lista das pessoas que estão acima da média de idade:')
for p in lista_cadastro:
    if p['Idade'] > media_idade:
        print(f'   -> Nome: {p["Nome"]}; Sexo: {p["Sexo"]}; Idade: {p["Idade"]};')
