"""
DESAFIO 105

💡 Faça um programa que tenha uma função notas() que pode
receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.
"""

def notas(*num, sit=False):
    """
    :param num: notas dos alunos
    :param sit: situação do aluno, caso queira ver = True
    :return: Retorna o valor do dicionário
    """
    armazenar_dict = dict()
    armazenar_dict['total'] = len(num)
    armazenar_dict['maior'] = max(num)
    armazenar_dict['menor'] = min(num)
    armazenar_dict['media'] = sum(num) / len(num)

    if sit:
        if armazenar_dict['media'] >= 7:
            armazenar_dict['situacao'] = 'Boa'
        if armazenar_dict['media'] >= 5:
            armazenar_dict['situacao'] = 'Razoável'
        else:
            armazenar_dict['situacao'] = 'Horrível'

    return armazenar_dict

resp = notas(5,10,4,6,sit=True)
print(resp)
help(notas)
