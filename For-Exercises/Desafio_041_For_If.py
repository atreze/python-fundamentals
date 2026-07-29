#Ler o primeiro termo e a razão de uma PA. Mostrar os 10 primeiros termos

print('PROGRESSÃO ARITMÉTICA')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Qual a razão: '))

for contador in range(1, 11):
    termo = primeiro_termo + (contador - 1) * razao
    print(termo)
