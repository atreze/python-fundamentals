#Leia duas notas e calcule a média, mostrando se está reprovado, aprovado, recuperação

preco_produto = float(input('Qual o preço do produto?'))

print('\nQual a forma de pagamento')
print('Opção 1: À vista')
print('Opção 2: À vista no cartão')
print('Opção 3: Em até 2x no cartão')
print('Opção 4: 3x ou mais no cartão\n')

opcao_pagamento = int(input('Escolha a opção: '))

a_vista = preco_produto - (preco_produto * 10 / 100)
a_vista_cartao = preco_produto - (preco_produto * 5 / 100)
cartao_3x = preco_produto + (preco_produto * 20 / 100)

if opcao_pagamento == 1:
    print('Valor do produto, à vista: {:.2f}'.format(a_vista))
elif opcao_pagamento == 2:
    print('Valor do produto, à vista no cartão: {:.2f}'.format(a_vista_cartao))
elif opcao_pagamento == 3:
    print('Valor do produto, em até 2x: {:.2f}'.format(preco_produto))
elif opcao_pagamento == 4:
    print('Valor do produto, 3x ou mais no cartão: {:.2f}'.format(cartao_3x))
else:
    print('Opção inválida, tente novamente')
