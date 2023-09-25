produtos_precos = { 'banana': 2.0, 'maçã': 1.5,  'laranja': 1.0,'uva': 3.0,  'morango': 2.5}


lista_de_compras = ['banana', 'maçã', 'uva', 'laranja', 'banana']


valor_total = sum(produtos_precos[produto] for produto in lista_de_compras)
print(f"o valor total da lista e R$  {valor_total}")