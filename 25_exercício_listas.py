#Receba 10 valores e exiba a soma de todos eles
x = [int(input("Digite um número: ")) for i in range(0,3) ]

soma = 0
for i in x:
        soma = soma + i

print(f"Soma = {soma}")