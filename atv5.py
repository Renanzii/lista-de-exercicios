nome = input("digite o nome: ")
primeira_nota = float(input("digite a primeira nota : "))
segunda_nota = float(input("digite a segunda nota : "))

media = primeira_nota + segunda_nota / 2

if media >= 0 and  5:
    print(f"{nome} sua nota e {media} Reprovado ")
elif media >= 5 < 7:
    print(f"{nome} sua nota e {media} Recuperação ")    
elif media >= 7 <= 10: 
    print(f"{nome} sua nota e {media} Aprovado ")    
