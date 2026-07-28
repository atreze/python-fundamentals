#Fazer um programa de aprovação de empréstimo. Vai perguntar valor da casa, salário e
#em quantos anos ele vai pagar.

salario = float(input('Qual o valor do seu salário: '))
valor_casa = float(input('Qual o valor da casa: '))
anos_para_pagar = int(input('Em quantos anos pretende pagar a casa: '))

valor_prestacao_mensal = (valor_casa/(anos_para_pagar*12))
limite_prestacao = salario*0.30

print('Valor prestação {:.2f}'.format(valor_prestacao_mensal))
print('Valor que não pode exceder: {:.2f}'.format(limite_prestacao))

if valor_prestacao_mensal > limite_prestacao:
    print('Infelizmente seu empréstimo não foi aprovado!')
else:
    print('Parabéns!!, empréstimo aprovado')
