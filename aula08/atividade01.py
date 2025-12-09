# Cadastrar 3 vendedores
# Cada vendedor deve ser armazenado, contendo as seguintes informações:
# nome
# vendas - armazenar 5 vendas, representando os valores das vendas realizadas
# total - armezanar a soma das vendas (calcular)
# média - armazenar a media das vendas (calcular)
# Após o cadastro, o programa deve exibir dos dados completos de cada um:
# Nome, lista das vendas, total e média

vendedores = []

for v in range(1):
    nome = input('\nInforme o nome do vendedor: ')   

    lista_vendas = []
    for l in range(2):
        venda = float(input('Informar o valor das vendas: '))
        lista_vendas.append(venda)
       

    soma = sum(lista_vendas)
    media = sum(lista_vendas) / len(lista_vendas) 
    
    vendedor = {
        'Nome': nome,
        'Lista de vendas': lista_vendas,
        'Total': soma,
        'Media': media
    }

    vendedores.append(vendedor)

for colaborador in vendedores:
    print(f'Nome: {colaborador ["Nome"]}')
    print(f'Lista de vendas: {colaborador ["Lista de vendas"]}')
    print(f'Total: {colaborador ["Total"]}')
    print(f'Media: {colaborador ["Media"]}\n')

    

