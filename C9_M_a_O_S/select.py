import math


def partition_around(A, p, r, x):
    # Find the index of the pivot value x and move it to the end
    for idx in range(p, r + 1):
        if A[idx] == x:
            A[idx], A[r] = A[r], A[idx]
            break

    # Standard Lomuto partition around the value now at A[r]
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def select(A, p, r, i):
    # 1. Handle blocks until subarray size is a multiple of 5
    while (r - p + 1) % 5 != 0:
        for j in range(p + 1, r + 1):
            if A[p] > A[j]:
                A[p], A[j] = A[j], A[p]
        if i == 1:
            return A[p]
        p = p + 1
        i = i - 1

    # 11. Calculate the number of 5-element groups
    g = (r - p + 1) // 5

    # 12. Sort each interleaved 5-element group in place
    for j in range(p, p + g):
        # Gather indices for the current group
        idx = [j, j + g, j + 2 * g, j + 3 * g, j + 4 * g]
        # Sort values corresponding to these indices
        vals = sorted([A[k] for k in idx])
        # Place sorted values back into the interleaved locations
        for step, k in enumerate(idx):
            A[k] = vals[step]

    # 16. Recursively find the median of medians (which now lie in A[p + 2g ... p + 3g - 1])
    x = select(A, p + 2 * g, p + 3 * g - 1, math.ceil(g / 2))

    # 17. Partition around the chosen pivot value x
    q = partition_around(A, p, r, x)

    # 19. Core selection logic (similar to Randomized-Select)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return select(A, p, q - 1, i)
    else:
        return select(A, q + 1, r, i - k)


# Example test case: Finding the 6th smallest element (i=6) in a scrambled array
data = [12, 3, 5, 7, 4, 19, 26, 2, 94, 68, 11, 23, 15, 8, 41]
target_statistic = 6  # 6th smallest element should be 8

# Running select (using 0-indexed boundaries for array pointers, but 1-indexed for statistics i)
result = select(data, 0, len(data) - 1, target_statistic)
print(result)
