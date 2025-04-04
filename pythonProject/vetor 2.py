vetor_1=[0]*10
vetor_2=[0]*10
n1=0
n2=0
i=0
for i in range(10):
  n1+=1
  vetor_1[i]+=(i+1)*5

j=0
for j in range(10):
  n2+=1
  vetor_2[j]+=j
print(vetor_1)
print(vetor_2)
print(n1)
print(n2)