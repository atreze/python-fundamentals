#leia duas notas, calcule media e mostre a nota final

nota_1 = int(input('Digite a primeira nota: '))
nota_2 = int(input('Digite a segunda nota: '))

media = (nota_1 + nota_2) / 2

if media < 5:
    print('Reprovado, sua nota foi de {} '.format(media))
elif 5 <= media <= 6.9:
    print('Recuperação, sua nota foi de {}'.format(media))
elif media >= 7:
    print('Aprovado, sua nota foi de {}'.format(media))
