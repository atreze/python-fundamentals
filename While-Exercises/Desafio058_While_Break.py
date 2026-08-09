#crie um programa que simule um caixa eletrônico. Pergunte o valor que será sacado e
#informe quantas células de cada valor serão entregues.
#Considere que o caixa possua células de 50,20,10 e 1.

print('=' * 60)
print(f'{"CAIXA ELETRÔNICO":^60}')  # O :^40 centraliza o texto em 40 espaços!
print('=' * 60)

saque = int(input('Digite o valor inteiro que será sacado: '))

celula_50 = saque//50
saque = saque % 50

celula_20 = saque//20
saque = saque % 20

celula_10 = saque//10
saque = saque % 10

celula_1 = saque//1

print('\n==========INICIANDO CONTAGEM DE NOTAS===============\n')

if celula_50 > 0:
    print(f'Total de {celula_50} cédula(s) de R$ 50')

if celula_20 > 0:
    print(f'Total de {celula_20} cédula(s) de R$ 20')

if celula_10 > 0:
    print(f'Total de {celula_10} cédula(s) de R$ 10')

if celula_1 > 0:
    print(f'Total de {celula_1} cédula(s) de R$ 1')

print('\nFinalizando transação...')
