#faça um codigo que leia N numeros do usuario e salve em um arquivo

numero = int(input("digite o numero: "))


with open ('ArquivoN.TXT','r') as arquivo:
    for n in numero:
        number = (input("digite o numero:"))

    arquivo.write(F"{number}\n")
    arquivo.write()

with open ('Num.TXT', 'w') as arquivo:
     som = 0
     quant = 0
for line in arquivo:
    number = int(line)
    resp = som + number
    quant += 1
    r = resp/quant
    (print (f"e {r} "))
        





