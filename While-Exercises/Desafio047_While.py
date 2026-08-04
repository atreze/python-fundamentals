#Criar um programa que leia dois valores e mostre um menu na tela

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

print('---------MENU------------')
print('[1] Somar')
print('[2] Multiplicar')
print('[3] Maior')
print('[4] Novos números')
print('[5] Sair')

opcao = 0

while opcao != 5:
    opcao = int(input('OPÇÃO: '))
    if opcao == 1:
        print('A soma é {}'.format(n1 + n2))
    elif opcao == 2:
        print('A multiplição {}'.format(n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O maior é o {}'.format(n1))
        else:
            print('O maior é o {}'.format(n2))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!!')
