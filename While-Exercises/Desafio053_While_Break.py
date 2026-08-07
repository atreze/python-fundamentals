#números foram digitados e a soma entre eles.

contador = 0
soma = 0

while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'Foram digitados {contador} números e a soma entre eles é {soma}')
