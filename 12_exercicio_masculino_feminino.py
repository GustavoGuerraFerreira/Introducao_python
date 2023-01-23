#Receba F para feminino e M para masculino e exiba o sexo da pessoa
sexo = input("Digite F para feminino e M para masculino: ")

if sexo == 'f' or sexo == 'F':
    print('Seu sexo é Feminino')
elif sexo == 'm'or sexo == 'M':
    print('Seu sexo é Masculino')
else:
    print('valor inválido')