#Verificar se o nome da cidade começa com "Santo"
cidade = input('Digite o nome da cidade: ').strip()
buscapalavra_santo = cidade.lower().startswith('santo')

print('É verdade que o nome da cidade começa com "Santo"?:', buscapalavra_santo)
print()

#Verificar se possui Silva no nome
nome = input('Digite o seu nome: ')
buscapalavra_silva = 'silva' in nome.lower().split()
print('É verdade que no nome {} possui Silva?:'.format(nome),buscapalavra_silva)
