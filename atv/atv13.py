n = (2,4,6,8,10,15)

todos_pares = all(num % 2 == 0 for num in n)


if todos_pares:
    print("todos os elementos são pares")
else:
    print("alguns elementos não são pares")    
