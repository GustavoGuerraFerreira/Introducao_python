#Mesclagem de tipo de dados, listas em dicionários
x = {'nomes': [], 'idade': 21}
x['nomes'].append('Gustavo Guerra')
x['nomes'].append('Marcio Braga')
print(x['nomes'][0])

#Mesclagem de tipo de dados, dicionário em listas

pessoas = [ { 'Nome': 'Gustavo', 'idade': 20, 'cep': 1414234124 },
            { 'Nome': 'Marcio', 'idade': 20, 'cep': 1414234124 },
            { 'Nome': 'Debora', 'idade': 20, 'cep': 1414234124 }]

for pessoa in pessoas:
    print(pessoa['Nome'])