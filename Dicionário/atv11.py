paises_capitais = {'Brasil': 'Brasília','Estados Unidos': 'Washington, D.C.','França': 'Paris','Japão': 'Tóquio','Índia': 'Nova Delhi'}


def pesquisar_capital(pais):
    if pais in paises_capitais:
        return paises_capitais[pais]
    else:
        return 'País não encontrado no dicionário.'


pais_pesquisado = input('Digite o nome de um país para saber sua capital: ')


capital = pesquisar_capital(pais_pesquisado) 
print(capital)