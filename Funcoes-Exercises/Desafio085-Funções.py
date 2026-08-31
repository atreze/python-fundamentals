#Crie um programa que tenha uma função chamada voto()
# Vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem:
#voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

from datetime import date

def voto(ano):
    ano_atual = date.today().year
    idade = int(ano_atual - ano)
    if idade < 16:
            return f'Você tem {idade} e seu voto ainda é: NEGADO!'
    elif (16 <= idade < 18) or (idade >= 70):
        return f'Você tem {idade} e seu voto é: OPCIONAL!'
    else:
        return f'Você tem {idade} e seu voto é: OBRIGATÓRIO!'

ano_nascimento = int(input('Digite o seu ano de nascimento: '))
print(voto(ano_nascimento))
