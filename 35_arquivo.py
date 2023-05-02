arquivo = open('pessoas.txt', 'a')
i = 0
while True:
    if i > 1:
        break
    arquivo.write(input("Digite o nome da pessoa: ") + " " + input('Digite a Idade ') + "\n")
    i += 1