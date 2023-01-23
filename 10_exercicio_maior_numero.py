#Receba 3 números inteiros e exiba o maior deles
n1  = int(input('Digite o primeiro número: '))
n2  = int(input('Digite o segundo número: '))
n3  = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'número 1 é o maior, {n1}')
elif n2 > n1 and n2 > n3:
    print(f'número 2 é o maior, {n2}')
else:
    print(f'número 3 é o maior, {n3}')