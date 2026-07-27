##Pergunte a distância em KM da viagem. Até 200 km cobrar 0.50 por KM, acima disso
#0,45

distancia_viagem = float(input('Digite a distância da viagem: '))

if distancia_viagem <= 200:
    print('O valor da sua viagem é R${:.2f}'.format(distancia_viagem * 0.50))
else:
    print('O valor da sua viagem é: R${:.2f}'.format(distancia_viagem * 0.45))
