#Receba um número inteiro do usuário e mostre a tabuada desse número.

numero = int(input("Digite qual número deseja saber a tabuada: "))
i = 0

while i <= 10:
    mult = numero * i
    print(f"{numero } x {i} = {mult}")
    i += 1