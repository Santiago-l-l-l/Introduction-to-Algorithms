import random


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


def randomized_select(A, p, r, i):
    if p == r:
        return A[p]

    q = randomized_partition(A, p, r)
    k = q - p + 1

    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)


data = [12, 3, 5, 7, 4, 19, 26, 2, 8]
target_statistic = 6  # 6th smallest element is 8
result = randomized_select(data, 0, len(data) - 1, target_statistic)
print(result)
