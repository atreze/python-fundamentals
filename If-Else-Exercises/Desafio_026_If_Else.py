#Ler três comprimentos e falar se pode ou não formar um triângulo

medida_1 = int(input('Digite o valor da primeira reta: '))
medida_2 = int(input('Digite o valor da segunda reta: '))
medida_3 = int(input('Digite o valor da terceira reta: '))

if medida_1 + medida_2 > medida_3 and \
   medida_1 + medida_3 > medida_2 and \
   medida_2 + medida_3 > medida_1:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')
