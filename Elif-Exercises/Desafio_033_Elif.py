#ler o peso e altura, calcular IMC e mostrar o status.

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = (peso / (altura**2))

if imc < 18.5:
    print('Abaixo do peso, IMC {:.2f}'.format(peso, imc))
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal, IMC {:.2f}'.format(peso, imc))
elif imc >= 25 and imc <= 30:
    print('Sobrepeso, IMC {:.2f}'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Obesidade, IMC {:.2f}'.format(imc))
elif imc >40:
    print('Obesidade Mórbida, IMC {:.2f}'.format(imc))
