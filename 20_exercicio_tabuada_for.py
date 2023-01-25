#Receba um número e mostra a tabuda completa dele usando o laço for.

n1 = int(input("Digite um número: "))

for i in range(0, 11):
    print(f"{n1} x {i} = {n1*i}")