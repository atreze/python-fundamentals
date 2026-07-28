#Pergunte o salário do funcionário, acima de 1.250 aumento de 10%, abaixo ou igual é 15%

salario = float(input('Digite o valor do seu salário: '))

if salario <= 1250.00:
    print('Seu novo salário será R${}'.format((salario*0.15 + salario)))
    print('O aumento será de 15%, R${:.2f}'.format(salario * 0.15))
else:
    print("Seu novo salário será R${:.2f}".format(salario*0.10 + salario))
    print('O aumento será de 10%, R${:.2f}'.format(salario*0.10))
