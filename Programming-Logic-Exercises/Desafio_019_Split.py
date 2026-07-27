#Leia o nome da pessoa e mostre o nome dela separadamente

nome = input('Digite o seu nome: ').capitalize().strip()

resultado = nome.split()
print('Seu primeiro nome é:',resultado[0])
print('Seu último nome é:',resultado[-1].capitalize())
