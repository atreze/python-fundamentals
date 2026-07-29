#Fazer uma tabuada

numero_escolhido = int(input('Digite o número que queira ver a tabuada: '))

for contador in range(0,11):
    tabuada = numero_escolhido * contador
    print(tabuada)
