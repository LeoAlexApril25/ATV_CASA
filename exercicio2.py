velocidade_carro = float(input("Informe a velocidade do carro:"))
multa_Km=7

if velocidade_carro > 80 :
    multa = (velocidade_carro - 80)*7
    print(f"A multa por passar de 80 km foi de {multa}")
else:
    print("Ele não passou dos 80km, então sem necessidade de multa.")