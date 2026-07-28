#Ler a data de nascimento e mostrar categoria, conforme a idade.

ano_nascimento = int(input('Digite sua data de nascimento: '))
idade = (2026 - ano_nascimento)

if idade <= 9:
    print("Categoria mirim, idade: {}".format(idade))
elif idade <= 14:
    print("Categoria infantil, idade: {}".format(idade))
elif idade <= 19:
    print("Categoria junior, idade: {}".format(idade))
elif idade <= 20:
    print("Categoria senior, idade: {}".format(idade))
elif idade > 20:
    print("Categoria Master, idade: {}".format(idade))
else:
    print('Opção inválida')
