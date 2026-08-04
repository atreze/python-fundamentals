#ler um número inteiro e mostrar os n primeiros números de uma sequencia de fibonacci

numero_escolhido = int(input('Digite um número inteiro: '))

primeiro_numero = 0
segundo_numero = 1
contador = 0

while numero_escolhido != contador:
    terceiro_termo = primeiro_numero + segundo_numero
    contador += 1
    print(primeiro_numero)
    primeiro_numero = segundo_numero
    segundo_numero = terceiro_termo
