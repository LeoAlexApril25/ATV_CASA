vetor_n=[]
i=0

for i in range(7):
 nome = input("Escreva nome aqui:")
 vetor_n.append(nome)

print('------------------------')
print("O nome em chamada são:")
for nome in reversed(vetor_n):
    print(nome)
print('------------------------')

