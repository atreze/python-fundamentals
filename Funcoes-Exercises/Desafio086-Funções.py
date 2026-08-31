#Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional)
#indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(num, show=False):
    """
    :param num: número que deseja fatorar
    :param show: caso queira ver a fatoração, escolha true
    :return: retorna o valor da fatoração
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(10, show=False))
help(fatorial)
