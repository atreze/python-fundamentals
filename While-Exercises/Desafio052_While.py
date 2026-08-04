#Ler vários números inteiros. Mostrar média entre os valores e qual foi o menor ou maior.
#Precisa perguntar ao usuário se ele deseja continuar ou finalizar o programa.

maior = 0
menor = 0
numeros = []
while True:
    num = int(input('Digite os números inteiros: '))
    numeros.append(num)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if 'N' in continuar:
        break
media = sum(numeros)/len(numeros)
maior = max(numeros)
menor = min(numeros)
print(f'A média dos valores é {media:.2f}')
print(f'O maior número é o {maior} e o menor {menor}')
