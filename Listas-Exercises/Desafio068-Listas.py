#Crie um programa que leia vários números e coloque em uma lista.
#Criar duas listas extras, uma com números pares e a outra ímpares
#No final mostrar o conteúdo das três listas

lista_original = list()
lista_par = list()
lista_impar = list()

while True:
    print('-' * 20)
    n = int(input('Digite um número: '))
    lista_original.append(n)

    if n % 2 == 0:
        lista_par.append(n)
    if n % 2 != 0:
        lista_impar.append(n)

    resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta == 'N':
        break

print(f'Lista original: {lista_original}')
print(f'Lista par: {lista_par}')
print(f'Lista impar: {lista_impar}')
