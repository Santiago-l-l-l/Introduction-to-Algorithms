from math import *

def merge(A, p, q, r):
    nL=q -p +1
    nR= r -q

    L=[0]*nL
    R=[0]*nR

    for i in range(0, nL):
        L[i]=A[p+i]
    for j in range(0, nR):
        R[j]= A[q+j+1]

    i=0
    j=0
    k=p

    while i<nL and j<nR:
        if L[i] <= R[j]:
            A[k]=L[i]
            i=i+1
        else: 
            A[k]=R[j]
            j=j+1
        k=k+1

    while i<nL:
        A[k]=L[i]
        i=i+1
        k=k+1
    while j<nR:
        A[k]=R[j]
        j=j+1
        k=k+1


#The recursive function, using merge:

def merge_sort(A, p, r):
    if p<r:
        q=floor((p+r)/2)

        merge_sort(A, p, q)

        merge_sort(A, q+1, r)

        merge(A, p, q, r)

    


A = list(map(int, input("Enter space-separated numbers: ").split()))
print("\nYour array is: ", A)

merge_sort(A, 0, len(A)-1)

print('\nYour sorted array is: ', A)
