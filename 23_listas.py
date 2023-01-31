'''nomes  = ['João', 'Lucas', 'Matheus', 'Carlos']

nomes[0] = "Gustavo"
nomes.append('Estevão')
print(nomes)'''
''' 
nomes = []
while True:
    nome = input("Digite N para sair, ou cadastre um nome: ")
    if nome == "N":
        break
    nomes.append(nome)

print(nomes)'''
'''
nomes = ['Caio', 'Marcos' , 'Carlos', 'Pedro']
nomes.insert(1, 'Joao')
print(nomes)
'''

'''
nomes = ['Caio', 'Marcos' , 'Carlos', 'Pedro']

nomes.pop(1)
print(nomes)
'''
'''
nomes = ['Caio', 'Marcos' , 'Carlos', 'Pedro']
nomes.remove('Caio')
print(nomes)
'''
'''
nomes = ['Caio', 'Marcos' , 'Carlos', 'Pedro']
print(nomes.index('Carlos'))
print(nomes)
'''

'''
nomes = ['Caio', 'Marcos' , 'Carlos', 'Pedro']

nomes_ordenado= sorted(nomes, reverse = True)

print(nomes_ordenado)

'''

'''

'''

idades = [2, 3, 4,5,6,7,8,9,]

idades_pares = []
for i in idades:
    if i % 2 == 0:
        idades_pares.append(i)
print(idades_pares)

