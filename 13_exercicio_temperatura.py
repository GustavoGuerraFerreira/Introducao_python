#Receba uma temperatura em farenheit e exiba em graus celsius
# c = 5 * f - 32/9

temperatura_farenheit = float(input("Digite a temperatura em farenheit: "))

temperatura_celsius =  (temperatura_farenheit -32) * 5/9
print(f"A temperatura em graus celsius é {temperatura_celsius}")