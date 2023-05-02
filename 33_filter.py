x = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

x = list(filter(lambda x: x < 18 or x % 2 == 0, x))

print(x)

y = [{'nome': 'caio', 'idade' : 20}, {'nome': 'Marcos', 'idade' : 40}]

y = list(filter(lambda x: x['nome'] == 'Marcos', y))
print(y)