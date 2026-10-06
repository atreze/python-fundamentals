#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python
#só que fazendo a validação para aceitar apenas um valor numérico.

def leiaInt(texto_que_vai_aparecer):
    while True:
        num = (input(texto_que_vai_aparecer))
        if num.isnumeric():
            return int(num)
        else:
            print('\033[0;31mEntrada inválida, digite novamente\033[m')

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
print(f"O dobro do valor digitado é: {leiaInt('Digite um n: ') * 2}")  
