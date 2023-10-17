from pprint import  pprint



def ler_dados():
    n = input("digite o nome")
    idade = input("digite a idade")
    curso = input("digite o curso")



    dados_alunos = {
        "nome":n,
        "idade": idade,
        "curso": curso,
    }
    return dados_alunos



def criar_arquivo(dados_aluno):
        with open ("alunos.txt","w") as arquivo:
            for chave, valor in dados_aluno.itens():
                 linha = f'{chave}:{valor}\n'
                 arquivo.write(linha)

if __name__=='_main_':
     dados_aluno = ler_dados()
     criar_arquivo(dados_aluno=dados_aluno)                 