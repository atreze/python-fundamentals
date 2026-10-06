"""
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
OBS: use cores.
"""

def ajuda(comando):
   print(f'\033[1;95m~' * (len(comando) + 34))
   print(f'Acessando o manual do comando {comando}')
   print(f'~' * (len(comando) + 34) + '\033[m')
   help(comando)

def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca > ')).strip()

    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO!')
        break
    else:
        ajuda(comando)
