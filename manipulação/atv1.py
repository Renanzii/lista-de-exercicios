estudantes = {}


quant_estudantes = int(input("quantidade de estudantes:  "))


for i in range(quant_estudantes):
    nome = input("digite o nome: ")
    idade = input("digite a idade: ")
    curso = input("digite o curso: ")


estudantes [nome] = {"idade": idade, "curso": curso}


with open("estudantes.txt","w") as arquivo:
    for nome, infor in estudantes.items():
        arquivo.write(f"nome : {nome}, idade: {infor['idade']}, curso: {infor['curso']}\n")


print("informacoes dos estudantes no arquivo 'estudantes.txt'. ")        