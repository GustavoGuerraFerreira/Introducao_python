def soma_numeros(*args):
    soma = 0
    for i in args:
        soma = soma + i
    print(soma)

soma_numeros(1,2,3,4,5,6,7,8,9)

def soma_numeros2(**kwargs):
      x =kwargs.get('teste3')
      if x :
           print('foi passado')
      else:
           print('Não foi passado')

soma_numeros2(teste1 = 1, teste2 = 2, teste3 = 3)
