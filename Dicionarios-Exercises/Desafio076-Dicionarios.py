#Crie um programa que leia nome, ano de nascimento e CTPS. Cadastre os em um dicionário.
#Se CTPS diferente de 0, o dicionário também recebrá ano de contratação e o salário. Calcule e acrescente, além da idade
#quantos anos a pessoa vai se aposentar.

from datetime import datetime

cadastro = dict()

cadastro['Nome'] = str(input('Digite o nome: '))
cadastro['Ano de Nascimento'] = int(input('Digite o ano de nascimento: '))
cadastro['CTPS'] = int(input('Digite o número da carteira de trabalho [Diferente de 0]: '))
cadastro['Idade'] = datetime.now().year - cadastro['Ano de Nascimento']


if cadastro['CTPS'] != 0:
    print('=-'*20)
    print('Vamos precisar de mais alguns dados....')
    cadastro['Ano de contratação'] = int(input('Digite seu ano de contratação: '))
    cadastro['Salário'] = float(input('Digite o seu salário: '))
cadastro['Ano de Aposentadoria'] = (cadastro['Ano de contratação'] - cadastro['Ano de Nascimento']) + 35


print('-=-=-=-= Dados da Pessoa Cadastrada =-=-=-=-')
for p, v in cadastro.items():
    print(f'{p}:{v}')
