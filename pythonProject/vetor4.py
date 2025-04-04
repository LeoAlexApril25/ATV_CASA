vetor_1=[0]*10
vetor_2=[0]*10
i=3
j=5

for i in range(10):
    if i % 2==1:
      vetor_1[i]=5-2
    else:
      vetor_1[i]=3+2

for j in range(10):
    vetor_2[j]+=j

print(vetor_1)
print(vetor_2)
