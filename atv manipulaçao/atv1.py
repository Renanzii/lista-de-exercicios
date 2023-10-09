estudantes = {}
quant_estudantes = int(input("digite a quantidade de estudantes: "))

for i in range(quant_estudantes):
    nome = input("digite o nome: ")
    idade = input("digite a idade:")
    curso = input("digite o curso do aluno: ")

    estudantes[nome] = {"idade": idade, "curso":curso}


    with open("estudantes.txt", "w") as arquivo:
        for nome, info in estudantes.items():
            arquivo.write(f"nome: {nome},idade: {info['idade']},curso: {info['curso']}\n")

            print("informaçoes do estudante foram salvas  'estudantes.txt'.")