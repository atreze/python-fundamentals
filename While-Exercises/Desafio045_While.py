#Ler o sexo de uma pessoa, só aceita M ou F. Se estiver errado pedir digitação correta até
#ter o valor correto

n = 0

while n != 'M' and n != 'F':
    n = str(input('Digite o seu sexo: ')).upper()
    if n != 'M' and n != 'F':
        print('Digite novamente, errado!')
