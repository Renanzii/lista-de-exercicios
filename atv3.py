nome_1= input("digiteo nome: ")
data_um = input("digite a data de nascimento: ")
nome_2 = input("digite o nome: ")
data_dois = input("digite a data de nascimento: ")


ano_data_um = data_um[6:10]
ano_data_dois = data_dois[6:10]

ano_atual = input("digite o ano atual : ")

ano_atual = int(ano_atual)
ano_data_um = int(ano_data_um)
ano_data_dois = int(ano_data_dois)

idade_pessoa_1 = ano_atual - ano_data_um
idade_pessoa_2 = ano_atual - ano_data_dois


if idade_pessoa_1 > idade_pessoa_2:
    print(f"a {nome_1}e mais velha do que {nome_2}")
elif idade_pessoa_2 > idade_pessoa_1:
    print(f"a{nome_2} e mais velha do que {nome_1}")
elif idade_pessoa_1 == idade_pessoa_2:
    print("as idades sao iguais")
