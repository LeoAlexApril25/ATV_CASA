Distancia_viagem=float(input('Informe a distancia da viagem de onibus :'))

if Distancia_viagem <= 200:
    Preco_passagem=Distancia_viagem*0.50
    print(f"O preço dá passagem até ponto de 200km ou menos é {Preco_passagem}")
elif Distancia_viagem > 200:
    Preco_passagem = Distancia_viagem * 0.45
    print(f"O preço dá passagem até ponto que passa de 200km é {Preco_passagem}")
else:
    print("Erro, distancia não inserida")
