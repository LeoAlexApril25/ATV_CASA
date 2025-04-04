vetor_1=[]
vetor_2=[]

while True:
    n1= int(input("Digite o numero :"))
    vetor_1.append(n1)
    n2= int(input("Digite o segundo numero :"))
    vetor_2.append(n2)

    if vetor_1 == 7 :
        for i in range(0,7):
            vetor_1[i]+=1


    if vetor_2 == 7:
        for i in range(0, 7):
            vetor_2[i] += 1


    print( vetor_1)
    print(vetor_2)
