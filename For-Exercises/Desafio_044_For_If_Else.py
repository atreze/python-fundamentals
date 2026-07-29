#Ler nome, idade e sexo de 3 pessoas. A média de idade do grupo
#nome do homem mais velho, quantas mulheres têm menos

media_idade = 0
quantia_mulheres = 0
homem_velho = 0
nome_homem = ''

for contador in range(0,3):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite seu sexo: '))
    media_idade += idade / 3
    if (sexo.lower() == 'feminino' or sexo.lower() == 'f') and idade < 20:
        quantia_mulheres += 1
    if sexo.lower() == "m" or sexo.lower() == "masculino":
        if idade > homem_velho:
            homem_velho = idade
            nome_homem = nome
        #Aqui, ele vai atualizar o nome e idade conforme minha comparação, armazenando esses valores nas variáveis homem_velho e nome_homem

print(f'A quantidade de mulheres é:{quantia_mulheres}')
print('A média de idade dos 3 é:{:.2f}'.format(media_idade))
print('Nome do homem velho:',nome_homem)
