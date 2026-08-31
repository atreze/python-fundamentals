# Faça um programa que tenha uma função chamada contador(), que receba três
# parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada.

def contador(i,f,p):
    for c in range(i,f,p):
        print(c,end=' ')
    print()

contador(1,11,1)
contador(10,-1,-2)

print('-=' * 15)
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))

contador(ini, fim, pas)
