palavras = ["josé", "pedro","milena","renan","tobias","algusto costa"]

palavras_com_mais_de_cinco_letras =[ palavra for palavra in palavras if len(palavra) > 5]
print(palavras_com_mais_de_cinco_letras)