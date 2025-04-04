vetor_1=[0]*15
vetor_2=[0]*15
f=1
f1=0



for i in range(15):
    if i % 2 == 0:
     vetor_1[i] = f1
     f1+=f

    else:
        vetor_1[i] = f
        f += f1

print(vetor_1)

for j in range(15):
    vetor_2[j]=j

print(vetor_2)





