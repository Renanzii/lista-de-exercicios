países_populaçao =(("China",1412000000),("Paraguai",67040000),("Inglaterra",55098000))


país_mais_populoso = max(países_populaçao, key=lambda país: país[1])

print(país_mais_populoso)