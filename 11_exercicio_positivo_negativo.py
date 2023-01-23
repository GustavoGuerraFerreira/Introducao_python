#Receba um número e exiba se ele é positivo ou negativo

numero = float(input("Digite um número: "))

if numero < 0:
    print("É um número negativo")
elif numero > 0:
    print("É um número Positivo")
else:
    print("O número é zero")