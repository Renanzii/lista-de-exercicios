notas_alunos = { 'jose': [8.5, 7.0, 9.5, 6.0],'renan': [9.0, 8.0, 7.5, 8.5],   'felipe': [7.5, 7.5, 7.0, 8.0]}

def calcular_media(notas):
    return sum(notas) / len(notas)

medias_alunos = {}
for aluno, notas in notas_alunos.items():
    media = calcular_media(notas)
    medias_alunos[aluno] = media


notas_gerais = [nota for notas in notas_alunos.values() for nota in notas]
media_geral = calcular_media(notas_gerais)


for aluno, media in medias_alunos.items():
    print(f'A média de {aluno} é {media}')

print(f'A média geral da turma é {media_geral}')