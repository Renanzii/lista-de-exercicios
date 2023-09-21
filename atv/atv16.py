tupla_1 = (2,5,7,8,9)
tupla_2 = (3,6,9,10)
tupla_3 =()
# tuupla_soma = tuple(x + y for x, y in (tupla_1, tupla_2))
tupla_3 = tupla_1 + tupla_2
soma =0
for x in tupla_3:
    soma = x + soma

print(" tupla 1:", tupla_1)
print(" tupla 2:", tupla_2)
print("a soma das duas tuplas", soma)