#ler o peso de 3 pessoas e mostrar qual foi o menor e qual foi o menor

pesos = []

for contador in range(1, 4):
    peso = float(input(f'Digite o peso da {contador}° pessoa: '))
    pesos.append(peso)
    
print("\nMaior peso:",max(pesos), 'kg.')
print("Menor peso:",min(pesos), 'kg.')
