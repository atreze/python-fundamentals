#Crie um programa que tenha uma tupla do zero ao 20 por extenso
#Deverá ler um número de 0 a 20 e mostrá-lo na tela por extenso

numero_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove','dez','onze', 'doze', 'treze','quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    if 0 <= escolha <= 20:
        print(f'Você digitou o número {numero_por_extenso[escolha]}')
        break
    print("Digite novamente...")
