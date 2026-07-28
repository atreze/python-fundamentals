#Ler dois números e compará-los, o primeiro ou segundo valor é maior, ou são iguais.
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo: '))

if numero_1 > numero_2:
    print('O primeiro valor é maior que o segundo = ', numero_1)
elif numero_2 > numero_1:
    print('O segundo valor é maior que o primeiro = ', numero_2)
elif numero_1 == numero_2:
    print('Os números são iguais = ',numero_1,numero_2)
else:
    print('Opção inválida!!!')
