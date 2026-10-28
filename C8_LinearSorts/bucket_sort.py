def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key


def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]

    for i in range(0, n):
        bucket_index = int(n * A[i])
        B[bucket_index].append(A[i])

    for i in range(0, n):
        insertion_sort(B[i])

    output = []
    for i in range(0, n):
        output.extend(B[i])

    return output


data = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
sorted_data = bucket_sort(data)
print(sorted_data)