A = list(map(int, input("Enter space-separated numbers: ").split()))
print("Your array is: ", A)

for i in range(1, len(A)):
    key=A[i]
    # Insert A[i] into the sorted subarray A[i: i-1]
    j=i-1

    while j>0 and A[j] >key:
        A[j+1]=A[j]
        j=j-1
    A[j+1]=key

print('The sorted array is:', A)


