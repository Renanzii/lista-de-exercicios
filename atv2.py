velocidade_carro1 = float(input("digite a velocidade do carro1: "))
distancia_carro1 = float(input("digite a distancia do carro1: "))
velocidade_carro2 = float(input("digite a velocidade do carro2: "))
distancia_carro2 = float(input("digite a velocidade do carro2: "))

velocidade_carro1 = velocidade_carro1/distancia_carro1
velocidade_carro2 = velocidade_carro2/distancia_carro2

if velocidade_carro2 >velocidade_carro1:
    print("o carro 1 teve a maior velocidade media")

elif velocidade_carro1 > velocidade_carro2:
    print ("o carro 2 teve a maior velocidade media")


    print(f"velocidade media é {velocidade_carro1}")
    print(f"a velocidade media é {velocidade_carro2}")
    
