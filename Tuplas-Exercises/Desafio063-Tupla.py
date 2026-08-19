#Criar uma tupla com nome de produtos e respectivamente seu preço.
#No final mostrar uma listagem de preços organizando os dados em forma tabular.


produtos_e_precos = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 9.99,
)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for posicao in range(0, len(produtos_e_precos), 2):
    print(f'{produtos_e_precos[posicao]:.<30} R$ {produtos_e_precos[posicao+1]:>6.2f}')

print('-' * 40)

#:.<30: Pega o nome do produto, alinha à esquerda e preenche o restante dos 30 espaços com pontinhos .....
#:>6.2f: Pega o preço, alinha à direita reservando 6 espaços e garante 2 casas decimais para os centavos (ex: 15.90 em vez de 15.9).
#:^40: Centraliza o título "LISTAGEM DE PREÇOS" em um espaço de 40 caracteres.
