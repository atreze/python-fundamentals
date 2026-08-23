#Faça um programa que leia nome e media de um aluno, guardando a situação em um dicionario
#No final mostrar o conteúdo da estrutura na tela

aluno = dict()

aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Media'] = float(input('Digite a sua média:'))

if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    print('Reprovado')
    aluno['Situação'] = 'Reprovado'

print('Cadastro e Situação do Aluno')
print((aluno))
