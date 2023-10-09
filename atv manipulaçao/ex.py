
with open ('Aquivo.TXT','r') as arquivo:
    for linha in arquivo:
        print("-->" + linha)


with open ('Aquivo2.TXT','w') as arquivo:   
    arquivo.write("escreva no arquivo 1\n")
    arquivo.write("escreva no arquivo 2\n")



with open ('Aquivo2.TXT','r') as arquivo:    
    for linha in arquivo:
        print("-->" + linha)





