# Cadastrar 5 alunos
# Cada aluno deve conter o nome, 5 notas que serão informadas pelo usuários na hora do cadastro e a média calculada com base nas notas informadas
# Exibir nome, lista de notas e média
# 

alunos = []

for n in range(2):
    print(f'\n----- Aluno {n + 1} -----')
    nome = input('Informe o nome do aluno: ')

    notas = []
    for i in range(2):
        nota = float(input(f'Informe a nota{i + 1}: '))
        notas.append(nota)

    media = sum(notas) / len(notas)   # Colocando Len, o numero pelo qual será divido muda, não fica atrleado a uma quantidade fixa
    print(media)

    aluno = {
        'Nome': nome,
        'Notas': notas,
        'Media': media
    }

    alunos.append(aluno)

# Exibindo os dados
for estudante in alunos:
    print(f'Nome: {estudante["Nome"]}')
    print(f'Notas: {estudante["Notas"]}')
    print(f'Media: {estudante["Media"]}\n')
    # print(estudante)   # daria pra fazer desta forma tbm
    

