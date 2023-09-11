list_1 = [1,2,3,4,5]
list_2 = [4,5,6,7,8]


conjut1 = set(list_1)
conjut2 = set(list_2)

element_em_comum = conjut1 & conjut2


if element_em_comum: 
    print("as listas têm em comum:" , element_em_comum)
else:
    print("as lista não tem nada em comum.")
