print('Nome em MAISC')
string1 = 'Ana Caroline Pereira Santos'
print(string1.upper())
print('\n')

print('Nome em MINUSC')
print(string1.lower())
print('\n')

print('Quantas letras ao todo desconsiderando os espaços em branco')
string2 = 'Coisa linda di mãe'
print('"Coisa linda di mãe"')
tamanho = len(string2.replace(' ', ''))
print(tamanho)
print('\n')

print('Quantas letras tem o primeiro nome')
string3 = 'Conta isso aqui pra mim'
print('"Conta isso aqui pra mim"')
separar = string3.split()
resul2 = len(separar[0])
print(resul2)


