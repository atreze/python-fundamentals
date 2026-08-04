#Uma tupla é uma variável do tipo coleção que aloca vários espaços na memória
#para armazenar uma sequência imutável (que não pode ser alterada) de elementos!

alimentos = ('Frango','Suco','Arroz','Maracujá')

#Caso queira acessar uma posição, sem precisar percorrer a tupla:
print('=============TUPLAS=====================')
print(f'Um único alimento: {alimentos[1]}')
print('='*40)
#----Tipos de For--------

#Se não precisar mostrar a posição, pois ele vai percorrer todos, utilizar for:
for comida in alimentos:
    print(f'Eu vou comer {comida}')
print('='*40)
for cont in range(0,len(alimentos)):
    print(f'Eu vou comer {alimentos[cont]} na posição {cont}')
print('='*40)
for posicao, comida in enumerate(alimentos):
    print(f'Eu vou comer {comida} que está na posição {posicao}')
print('='*40)
#Sorted organiza a tupla em ordem alfabética
print(sorted(alimentos))
print('='*40)
#Isso aqui junta as tuplas, e não soma.
a = (2,5,9,7)
b = (5,8)
c = a + b #a ordem altera os fatores
print(c)
print('='*40)
#Pra saber o tamanho da tupla, ou seja, conta as posições {len}:
print(len(c))
print('='*40)
#Saber quantas vezes se repete o elemento {count}:
print(c.count(5))
print('='*40)

#saber qual elemento está em determinada posição {index}:
print(c.index(5,2))
# o segundo valor é de qual posição você quer iniciar
print('='*40)

#Nas tuplas, em python, não tem problema misturar tipos:
pessoa = ('Ana', 97, 'F', 95)
print(pessoa)

#posso deletar a tupla inteira
del(pessoa)

#len(numeros): Conta quantos itens têm na caixa.

#sum(numeros): Soma todos os números da caixa.

#max(numeros): Acha o maior número da caixa.

#min(numeros): Acha o menor número da caixa.

#numeros.count(): Conta quantas vezes o número aparece.
