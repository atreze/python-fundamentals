#Desafio aula 4, ler comprimento do cateto oposto e do cateto adjacente de um
#triângula retangulo e mostrar comprimento da hipotenusa

import math

#Aqui é sem o módulo:
CO = int(input('Comprimento do cateto oposto: '))
CA = int(input('Comprimento do cateto adjacente: '))
CH = (CO**2 + CA**2) ** (1/2)
print("O comprimeto da hipotenusa é {:.2f}".format(CH))

#Com módulo. já possui função de utilizar cálculo da hipotenusa:
CH = math.hypot(CO,CA)
print("O comprimeto da hipotenusa é {:.2f}".format(CH))
