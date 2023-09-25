estoque_produtos = {'Camisetas': 50,'Calças': 30,'Bonés': 10,'Sapatos': 20,'Meias': 5}


estoque_minimo = 15


produtos_baixo_estoque = []

for produto, estoque in estoque_produtos.items():
    if estoque < estoque_minimo:
        produtos_baixo_estoque.append(produto)


print("Produtos com estoque abaixo do valor mínimo:")
for produto in produtos_baixo_estoque:
    print(f'{produto}: {estoque_produtos[produto]} unidades')