#Criar um programa que leia nome e duas notas, vários alunos, guardar em uma lista.
#No final mostrar um boletim contendo a média de cada e permita que o usuário possa
#ver a nota individual de cada um.


alunos = []
temporario = []



while True:
    temporario.append(str(input('Digite o nome do aluno: ')))
    temporario.append(float(input('Digite a primeira nota do aluno: ')))
    temporario.append(float(input('Digite a segunda nota do aluno: ')))

    alunos.append(temporario[:])

    temporario.clear()
    print('-=' * 17)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? APENAS [S/N] ')).upper()
        if len(resposta) > 0:
            resposta = resposta[0]
    if resposta == 'N':
        break

print('-=' * 23)
print('BOLETIM DOS ALUNOS DA ESCOLA DRA. ANA CAROLINE')
print('-=' * 23)
for a in alunos:
    media = (a[1] + a[2]) / 2
    print(f'O aluno {a[0]} teve uma média de {media:.1f}')

print('-=' * 23)
individual = str(input('Deseja ver a nota individual de cada aluno? [S/N] ')).upper()
if individual == 'S':
    print('-=' * 18)
    for al in alunos:
       print(f'Aluno {al[0]}, teve nota 1°: {al[1]} e 2°: {al[2]}')
