cidades_estados = {'Nova York': 'Nova York','Los Angeles': 'Califórnia','Chicago': 'Illinois','Miami': 'Flórida','Austin': 'Texas','Seattle': 'Washington','Phoenix': 'Arizona','Denver': 'Colorado','Boston': 'Massachusetts', 'Dallas': 'Texas'}


estados_sem_repeticao = list(cidades_estados)

print("Estados sem repetição:")
for estado in estados_sem_repeticao:
    print(estado)