filmes = {'Matrix': 1999, 'jogos mortais 7': 2023, 'avatar 2': 2022, 'O Poderoso Chefão': 1972,'Forrest Gump': 1994}


filmes_ordenados = dict(sorted(filmes.items(), key=lambda item: item[1]))


for filme, ano in filmes_ordenados.items():
    print(f'{filme} ({ano})')