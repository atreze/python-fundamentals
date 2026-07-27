#Programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos

numero = input('Digite um número de 0 a 9999: ')

print('milhar',numero[0])
print('dezena:',numero[1])
print('centena:',numero[2])
print('unidade',numero[3])

#Esqueci de testar com menos números e dá erro, porque ele só vai aceitar sendo 4.
#Aqui precisaria usar um laço de repetição, mas como o professor ainda não passou
#ele utilizou math. Divisão do número utilizando o resto dele. Ex: u = numero // 1 % 10
