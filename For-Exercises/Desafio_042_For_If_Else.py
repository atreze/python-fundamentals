#ler o ano de nascimento de 4 pessoas. Mostrar quantas ainda não são maiores e os menores
maiores = 0
menores = 0

for contador in range(0,4):
    data_nascimento = int(input('Digite sua dasta de nascimento: '))

    idade = 2026 - data_nascimento

    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print('Maiores de idade: {}'.format(maiores))
print('Menores de idade: {}'.format(menores))
