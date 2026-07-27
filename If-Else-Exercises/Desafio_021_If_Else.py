#Ler a velocidade do carro, se ultrapassar 80km/h pagará 7,00 por KM ultrapassado.

velocidade_carro = int(input('Qual a velocidade do carro em km/h? '))

if velocidade_carro > 80:
    multa = (velocidade_carro - 80) * 7
    print('Você infringiu as leis de trânsito, sua multa é de R${:.2f} reais'.format(multa))
else:
    print('Parabéns, você é um bom condutor!!')
print('=== BOA VIAGEM ===')
