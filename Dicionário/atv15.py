alimentos_calorias = { 'Arroz': 150,  'Feijão': 200,'Frango grelhado': 250,'Salada de alface': 30,'Batata frita': 350,'Refrigerante': 150}


refeicao = ['Arroz', 'Feijão', 'Frango grelhado']


total_calorias = sum(alimentos_calorias.get(alimento, 0) for alimento in refeicao)

print(f'O total de calorias consumidas na refeição é {total_calorias} calorias.')