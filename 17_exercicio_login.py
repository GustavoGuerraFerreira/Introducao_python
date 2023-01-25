#Defina um usuário e senha e depois verifique se 
#login do usuário é valido
login = "login"
senha = "123"
while True:
    login_in = input("Digite o login: ")
    senha_in = input("Digite sua senha: ")
    if login == login_in and senha == senha_in:
        print("login do usuário é valido")
        break
    print("login do usuário inválido")