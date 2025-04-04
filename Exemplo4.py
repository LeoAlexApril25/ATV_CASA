Ano_atual=int(input("Informe o ano atual :"))

if  Ano_atual % 4 == 0:
    print("Esse ano é bissexto")

elif Ano_atual % 100 == 0:
    print("Esse ano é bissexto")

elif Ano_atual % 400 == 0:
    print("Esse ano não é bissexto")

else:
    print("Esse ano não é bissexto")
