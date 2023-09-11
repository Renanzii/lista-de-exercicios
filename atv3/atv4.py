list_de_compras = []


while True:
    item = input("digite os itens que deseja adicionar (ou  digite 'parar'para sair : )")
    if item =='parar':
        break


    list_de_compras.append(item)


print("sua lista")
for item in list_de_compras:
    print(item)