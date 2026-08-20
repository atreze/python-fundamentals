#Criar uma matriz 3x3 e preencher com valores lidos pelo teclado.
#No final mostrar a matriz com a formatação correta

matriz = [[], [], []]

for i in range(0,9):
    n = int(input(f'Digite o {i+1} número: '))
    linha = i // 3
    matriz[linha].append(n)

for linha in matriz:
    print(linha)
