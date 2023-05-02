from pympler.asizeof import asizesof

def dobro (lista):
    lista_dobro = []
    for i in lista:
        lista_dobro.append(i*2)
    return lista_dobro
def dobro2(lista):
    for i in lista:
        yield i * 2
y = asizesof(dobro2(range(0,1000)))
x = asizesof(dobro(range(0,100)))

print(x, y)