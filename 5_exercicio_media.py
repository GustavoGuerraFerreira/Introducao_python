#Escreva um Programa onde o usuário digite duas notas e ele mostra a média das duas notas

#pegar as notas:
nota1 = int(input("Digite a sua Primeira Nota: " ))
nota2 = int(input("Digite a sua Segunda Nota: "))
#Fazer a média
media = (nota1 + nota2) / 2
#Mostrar a média e notas:
print(f"Sua primeira nota foi {nota1} e sua Segunda nota foi {nota2}")
print(f"A sua média é {media}")
