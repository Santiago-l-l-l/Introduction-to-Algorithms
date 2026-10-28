def counting_sort_for_radix(A, exp):
    n = len(A)
    B = [0] * n
    C = [0] * 10

    for i in range(0, 10):
        C[i] = 0

    for j in range(0, n):
        digit = (A[j] // exp) % 10
        C[digit] = C[digit] + 1

    for i in range(1, 10):
        C[i] = C[i] + C[i - 1]

    for j in range(n - 1, -1, -1):
        digit = (A[j] // exp) % 10
        B[C[digit] - 1] = A[j]
        C[digit] = C[digit] - 1

    for j in range(0, n):
        A[j] = B[j]


def radix_sort(A, d):
    exp = 1
    for i in range(1, d + 1):
        counting_sort_for_radix(A, exp)
        exp *= 10


data = [329, 457, 657, 839, 436, 720, 355]
digits = 3
radix_sort(data, digits)
print(data)
