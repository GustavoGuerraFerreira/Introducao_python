#Faça um programa que o usuário possa cadastrar n pessoas,
#armazenando seu nome, idade e altura


pessoas = []
while True:
    num = int(input("Digite 1 para cadastrar ou 0 para sair: "))
    if num == 0:
        break
    Nome = input("Digite o nome Completo: ")
    Idade = int(input("Digite sua idade: "))
    Altura = float(input("Digite sua altura: "))
    pessoa = {'Nome' : Nome, 'Idade': Idade, "Altura": Altura }
    pessoas.append(pessoa)
print(pessoas)
