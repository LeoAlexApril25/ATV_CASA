import random

vetor = [0]*7
i=0
if len(vetor) == 7:
 for i in range(7):
     vetor[i]= random.randint(1,100)
     print(vetor)