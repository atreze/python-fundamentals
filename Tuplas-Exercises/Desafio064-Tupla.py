#crie um programa que tenha uma tupla com palavras sem acento, mostre as vogais de
#cada uma

palavras = ('python', 'programacao', 'estudo', 'teclado', 'codigo')

for p in palavras:
    print(f'Na palavra {p.upper()} temos as vogais: ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra)
