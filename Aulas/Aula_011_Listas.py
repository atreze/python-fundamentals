# =========================================================
# LISTAS
# =========================================================

# 1. CRIAÇÃO DE LISTAS
lista_vazia = []  # ou list()
numeros = [10, 20, 30, 40, 50]
misturada = [1, 'Python', 3.14, True]


# 2. ADICIONAR ELEMENTOS
numeros.append(60)        # Adiciona número no FINAL da lista
numeros.insert(0, 5)  # Adiciona na POSIÇÃO especificada -> insert(índice, valor)


# 3. REMOVER ELEMENTOS
numeros.pop()             # Remove e retorna o ÚLTIMO elemento
numeros.pop(0)            # Remove o elemento da POSIÇÃO informada
numeros.remove(30)        # Remove a PRIMEIRA ocorrência do VALOR 30 (dá erro se não existir)
del numeros[1]            # Deleta o elemento pelo índice usando comando nativo


# 4. CONSULTA E VERIFICAÇÃO
tamanho = len(numeros)    # Quantidade de elementos na lista
maior = max(numeros)      # Maior valor
menor = min(numeros)      # Menor valor
soma = sum(numeros)       # Soma de todos os números
qtd = numeros.count(20)   # Quantas vezes o valor 20 aparece na lista

if 20 in numeros:         # Testa se o valor EXISTE na lista antes de buscar ou remover
    pos = numeros.index(20) # Devolve o ÍNDICE da PRIMEIRA ocorrência do valor 20


# 5. ORDENAÇÃO
numeros.sort()            # Ordena a própria lista em ORDEM CRESCENTE (modifica a original)
numeros.sort(reverse=True)# Ordena em ORDEM DECRESCENTE
lista_nova = sorted(numeros) # Cria uma NOVA lista ordenada sem alterar a original


# 6. PERCORRER LISTAS (LAÇOS)
# A) Apenas pelos valores:
for val in numeros:
    print(val)

# B) Pegando ÍNDICE e VALOR ao mesmo tempo (O mais usado!):
for pos, val in enumerate(numeros):
    print(f'Na posição {pos} temos o valor {val}')


# 7. MACETES ÚTEIS DO DIA A DIA

# Pegar o último item sem saber o tamanho:
ultimo = numeros[-1]
penultimo = numeros[-2]

# Fatiamento (Slicing): [início : fim : passo]
primeiros_tres = numeros[:3]   # Do início até o índice 2
ultimos_dois = numeros[-2:]    # Os dois últimos
invertida = numeros[::-1]      # Copia a lista inteira de trás para frente

# Copiar uma lista do jeito CERTO:
# Errado: A = B (Se alterar A, altera B junto!)
# Certo:
copia = numeros.copy()         # ou copia = numeros[:]

# Criar lista de números rápida com range:
sequencia = list(range(1, 11)) # Cria [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
