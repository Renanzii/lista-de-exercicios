salario = float(input("digite o salario: "))
finaciamento = float(input("qual o finaceiro: "))
if salario <= 0:
    print("seu salario nao pode ser negativo")
    salario = float(input("digite o salario: "))
if finaciamento <= 0:
    print("seu salario nao pode ser negativo")
finaciamento = float(input("qual o finaceiro: "))

if finaciamento <= salario * 5:
    print("financeiro concetido")
else:
    print("financeiro negado")
    print("obrigado por sua consulta")
    