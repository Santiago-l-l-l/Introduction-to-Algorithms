def counting_sort(A, k):
    n = len(A)
    B = [0] * n
    C = [0] * (k + 1)

    for i in range(0, k + 1):
        C[i] = 0

    for j in range(0, n):
        C[A[j]] = C[A[j]] + 1

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    for j in range(n - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1

    return B


data = [2, 5, 3, 0, 2, 3, 0, 3]
max_val = 5
sorted_data = counting_sort(data, max_val)
print(sorted_data)


