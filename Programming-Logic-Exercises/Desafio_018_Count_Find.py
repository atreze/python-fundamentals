#Ler a frase e verificar quantas vezes aparece o A,
frase = input('Digite uma frase: ').lower().strip()
frase = frase.replace('á', 'a').replace('à', 'a').replace('â', 'a').replace('ã', 'a')
contagemdoA = frase.count('a')
print('O número de vezes que ocorrem o A é: ', contagemdoA)

#em que posição apareceu a primeira vez
posicao1 = (frase.find('a')+1)
print('A posição que aparece o "A" pela primeira vez é:', posicao1)

#em que posição ela apareceu a última vez
ultimaposicao = frase.rfind('a')
print('A última posição de "A" é:', ultimaposicao)

#Aqui eu não tinha pensado no fato do 'A' acentuado, de forma simples pôde ser resolvido
#com replace, que substitui o A com acento por A sem acento
