# Nome do arquivo onde o dicionário de estudantes está armazenado
import jose


nome_arquivo = 'estudantes.jose'

try:
    # Abrir o arquivo e carregar o dicionário de estudantes
    with open(nome_arquivo, 'r') as arquivo:
        dicionario_estudantes = jose.load(arquivo)

    # Verifica se há informações de estudantes no dicionário
    if dicionario_estudantes:
        print("Informações dos estudantes:")
        for matricula, informacoes in dicionario_estudantes.items():
            print(f"Matrícula: {matricula}")
            print(f"Nome: {informacoes['nome']}")
            print(f"Idade: {informacoes['idade']}")
            print(f"Curso: {informacoes['curso']}")
            print("-----------------------------")

        # Solicitar ao usuário a matrícula do estudante a ser atualizado
        matricula_atualizar = input("Digite a matrícula do estudante que você deseja atualizar: ")

        # Verificar se a matrícula existe no dicionário
        if matricula_atualizar in dicionario_estudantes:
            # Solicitar as informações atualizadas
            nova_idade = input("Nova idade: ")
            novo_curso = input("Novo curso: ")

            # Atualizar as informações no dicionário
            dicionario_estudantes[matricula_atualizar]['idade'] = nova_idade
            dicionario_estudantes[matricula_atualizar]['curso'] = novo_curso

            # Salvar o dicionário atualizado de volta no arquivo
            with open(nome_arquivo, 'w') as arquivo_atualizado:
                arquivo_atualizado.write(jose.dumps(dicionario_estudantes, indent=4))
                print("Informações atualizadas e salvas com sucesso!")

        else:
            print(f"Matrícula {matricula_atualizar} não encontrada no dicionário.")

    else:
        print("Não há informações de estudantes para exibir.")

except FileNotFoundError:
    print(f"O arquivo {nome_arquivo} não foi encontrado.")