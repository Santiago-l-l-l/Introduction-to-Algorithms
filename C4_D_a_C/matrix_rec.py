

def matrix_multiply_recursive(A, B, C, n):
    if n==1:
        C[0][0]+= A[0][0]*B[0][0]
        return C
    
    # 5-6: Divide - Create 2D arrays for the n/2 x n/2 submatrices
    
    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]] 

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    C11 = [row[:mid] for row in C[:mid]]
    C12 = [row[mid:] for row in C[:mid]]
    C21 = [row[:mid] for row in C[mid:]]
    C22 = [row[mid:] for row in C[mid:]]

    # 7-15: Conquer - 8 recursive calls adding products directly into the C quadrants
    matrix_multiply_recursive(A11, B11, C11, mid)
    matrix_multiply_recursive(A11, B12, C12, mid)
    matrix_multiply_recursive(A21, B11, C21, mid)
    matrix_multiply_recursive(A21, B12, C22, mid)
    matrix_multiply_recursive(A12, B21, C11, mid)
    matrix_multiply_recursive(A12, B22, C12, mid)
    matrix_multiply_recursive(A22, B21, C21, mid)
    matrix_multiply_recursive(A22, B22, C22, mid)

    # Reassemble the updated submatrices back into C
    for i in range(mid):
        C[i] = C11[i] + C12[i]
    for i in range(mid):
        C[mid + i] = C21[i] + C22[i]

    return C


# --- Execution Test (Works on n x n matrices where n is a power of 2) ---
# Testing two 4x4 matrices

matrix_A = [[1,2,3,4],[5,6,7,8] ,[9,10,11,12] , [13, 14, 15, 16] ]

matrix_B = [[1, 0, 0, 0],[0,1,0,0] ,[0,0,1,0] , [0, 0, 0, 1] ] # Identity matrix


# Initialize a result matrix C filled with zeros
matrix_C = [[0] * 4 for _ in range(4)]

size = len(matrix_A)
result = matrix_multiply_recursive(matrix_A, matrix_B, matrix_C, size)

print("Result Matrix C:")
for row in result:
    print(row)




#------------------------------------------
#The rest of this is ai slop to write arbitrary matrices of size 2n. i got a bit lazy unu

def create_2n_matrix():
    # 1. Get the value of n
    try:
        n = int(input("Enter the value of n: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Calculate the actual size of the grid (2 * n)
    size = 2 * n
    print(f"\nCreating a {size}x{size} matrix...")

    matrix = []

    # 2. Collect matrix values row by row
    for i in range(size):
        while True:
            try:
                # Ask the user for a full row separated by spaces
                row_input = input(f"Enter row {i + 1} ({size} numbers separated by spaces): ")
                row = [float(x) for x in row_input.split()]
                
                # Validate that the row has exactly 2n elements
                if len(row) != size:
                    print(f"Error: Expected exactly {size} elements, but got {len(row)}. Try again.")
                    continue
                
                matrix.append(row)
                break
            except ValueError:
                print("Error: Please enter numbers only. Try again.")

    # 3. Print the resulting matrix cleanly
    print("\nYour final Matrix is:")
    for row in matrix:
        # Format numbers to look clean (strips .0 if it's an integer)
        print([int(x) if x.is_integer() else x for x in row])

    return matrix

print('\nTo multiply arbitrary matrices, first give A:')

A1=create_2n_matrix()

print('\nNow for B')
B1=create_2n_matrix()

C1 = [[0] * len(A1[0]) for _ in range(len(A1[0]))]

size1 = len(A1[0])
result1 = matrix_multiply_recursive(A1, B1, C1, size1)

print("Result Matrix C:")
for row in result1:
    print(row)