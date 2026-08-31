#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento)
# Mostre a área do terreno.

#area = largura * comprimento

def area(l, c):
    area_terreno = l * c
    print(f'A area de um terreno de {l:.2f} x {c:.2f} é de {area_terreno:.2f}m²')

print(f'--------------Controle de Terrenos----------------')
print('=-'*25)
l = int(input('LARGURA (m): '))
c = int(input('COMPRIMENTO (m): '))
area(l, c)
