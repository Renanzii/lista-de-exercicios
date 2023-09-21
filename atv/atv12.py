datas = [(11,9,2001),(1,4,1945),(20,9,2023)]

datas_ord = sorted(datas, key=lambda data: (data[2], data[1], data[0]))


print("datas ordenadas: ")
for data in datas_ord:
    print("{}/{}/{}".format(data[0], data[1], data[2]))