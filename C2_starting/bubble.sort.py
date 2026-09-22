

def bubble_sort(A):
    n=len(A)
    for i in range(0, n-1):
        for j in range(n-1, i, -1):
            if A[j]< A[j-1]:

                A[j], A[j-1]= A[j-1], A[j]


    return A


A = list(map(int, input("Enter space-separated numbers: ").split()))
print("\nYour array is: ", A)

bubble_sort(A)

print('\nYour sorted array is: ', A)