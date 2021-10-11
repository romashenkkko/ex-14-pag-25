l=int(input("Numarul de randuri: "))
A=[[int(input()) for i in range(n)] for j in range(n)]
for i in range(len(A)):
    print(A[i])
sum1 = 0
print("suma componentei diagoanelei principale este ", sum1)
for i in range(0,len(A)):
    sum1 += A[i][i]
sum2 = 0
for i in range(0,len(A)):
    sum2 += A[len(A)- i-1][i]
print("Suma componentelor diagonalei secundare este ", sum2)
sum3 = 0
for i in A:
    for j in i:
        if A.index(i)<i.index(j):
            sum3 += j
print("Suma componentelor mai sus de diagonala principala este ", sum3)
sum4 = 0
for i in A:
    for j in i:
        if A.index(i)>i.index(j):
            sum4+=j
print("suma componentelor mai jos de diagonala principala este ", sum4)
sum5 = 0
for i in A:
    for j in i:
        if A.index(i)+i.index(j)<n-1:
            sum5 += j
print("Suma componentelor mai sus de diagonala secundara este ", sum5)
s6 = 0
for i in A:
     for j in i:
        if A.index(i)+i.index(j)<n-1:
            sum6 += j
print("Suma componentelor mai jos de diagonala secundara este ", sum6)
