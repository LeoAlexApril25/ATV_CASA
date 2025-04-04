n1 = float(input("Informa a primeira nota :"))
n2 = float(input('informe a segunda nota:'))

m = (n1+n2)/2

if m >= 6.0:
    print("Sua média foi boa")

else:
    print('Sua média foi ruim')
    
print(f'Sua média é {m:.1f}')