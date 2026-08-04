#Ler vários números inteiros. Só vai parar quando digitar 999. No final mostrar quantos
#números foram digitados e qual foi a soma entre eles.

numero_escolhido = 0
soma = 0
contador = 0

while True:
    numero_escolhido = int(input('Digite os números [999 para parar]: '))
    if numero_escolhido == 999:
        break
    soma += numero_escolhido
    contador += 1

print(f'Você digitou {contador} números e a soma entre eles é {soma}.')
