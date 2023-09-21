frutas = ("maça","banana","graviola","morango","uva")


fruta_especifica ="morango"


if fruta_especifica in frutas:
    posiçao = frutas.index(fruta_especifica)
    print(f" a fruta {fruta_especifica} esta na posiçao {posiçao} na tupla")
else:
    print(f" a fruta {fruta_especifica} nao esta na  tupla")