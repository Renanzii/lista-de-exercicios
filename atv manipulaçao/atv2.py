import json


nome_arquivo = 'estudantes.json'


try:
    with open(nome_arquivo, 'r') as arquivo:
        dicionario_estudantes =json.load(arquivo)

if dicionario_estudantes:
    print("informaçoes do estudante")
    for matricula, informacoes in dicionario_estudantes.items():
        print(f"matricula:{matricula}")
        print(f"nome:{informacoes['nome']}")
        print(f"idade:{informacoes['idade']}")
        print(f"curso:{informacoes['curso']}")
        print("---------------------")
    else:
        print("não há informaçoes do estudante")

except FileExistsError:
print(f"o arquivo{nome_arquivo} nao foi encontrado")