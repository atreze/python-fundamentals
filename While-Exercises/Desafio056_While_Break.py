#Ler a idade e sexo de várias pessoas. A cada pessoa cadastrada perguntar se deseja continuar.
#No final mostrar:
# 1 - quantas pessoas tem mais de 18 anos
# 2 - Quantos homens foram cadastrados
# 3 - Quantas mulheres tem menos de 20 anos.

contador_idade = idade = 0
contador_homens = 0
contador_mulher = 0

while True:
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade > 18:
        contador_idade += 1
    if sexo == 'M':
        contador_homens += 1
    if sexo == 'F' and idade < 20:
        contador_mulher += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? Digite a opção correta: [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break

print('=' * 30)
print(f'{contador_idade} pessoa(s) com mais de 18 anos')
print(f'{contador_homens} homens foram cadastrados')
print(f'{contador_mulher} mulheres tem menos de 20 anos')
