#leia o ano de nascimento, informe se ainda vai se alistar, se já é hora de se alistar
#ou se já passou do tempo do alistamento
#Deve mostrar o tempo que falta ou que passou do prazo

ano_nascimento = int(input('Digite sua data de nascimento: '))
idade = (2026 - ano_nascimento)

if idade < 18:
    print('Ainda não está na hora, infelizmente faltam {} anos '.format(18 - idade))
elif idade == 18:
    print('Está na hora de se alistar querido, vá já pra guerra, macho!!!')
elif idade > 18:
    print('Se ainda não fez já deveria ter feito, irresponsável. Passou do tempo em {} anos!!'.format (idade - 18))
