# receba 4 notas de um aluno e exiba se ele foi aprovado (nota maior ou igual que 6)
#se ele ficou de recuperação (nota maior ou igual a 4) 
# ou se ele foi reprovado (nota menor do que 4)


nota1 = float(input('digite sua nota1: '))
nota2 = float(input('digite sua nota2: '))
nota3 = float(input('digite sua nota3: '))
nota4 = float(input('digite sua nota4: '))

media = (nota1+nota2+ nota3+nota4)/4

if media >= 6:
    print(f'aprovado, nota= {media}')
elif media >= 4:
    print(f'recuperação, nota = {media}')
else:
    print(f'reprovado, nota = {media}')