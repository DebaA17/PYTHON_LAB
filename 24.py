def multiply_matrices(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


# Take user input for matrices
def get_matrix(rows, cols):
    print(f"Enter elements for a {rows}x{cols} matrix (row-wise):")
    return [[int(input()) for _ in range(cols)] for _ in range(rows)]

rows_A = int(input("Enter number of rows for Matrix A: "))
cols_A = int(input("Enter number of columns for Matrix A: "))
rows_B = int(input("Enter number of rows for Matrix B: "))
cols_B = int(input("Enter number of columns for Matrix B: "))

if cols_A != rows_B:
    print("Matrix multiplication not possible. Columns of A must equal rows of B.")
else:
    A = get_matrix(rows_A, cols_A)
    B = get_matrix(rows_B, cols_B)
    result = multiply_matrices(A, B)
    print("Result:")
    for row in result:
        print(row)
