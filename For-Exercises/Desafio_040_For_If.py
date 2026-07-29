#Ler 6 números inteiros e mostrar apenas soma dos pares.

s = 0

for contador in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print(s)
