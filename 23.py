
# Program to add two matrices
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of first matrix:")
mat1 = []
for i in range(rows):
    mat1.append([int(x) for x in input().split()])

print("Enter elements of second matrix:")
mat2 = []
for i in range(rows):
    mat2.append([int(x) for x in input().split()])

result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(mat1[i][j] + mat2[i][j])
    result.append(row)

print("Sum of matrices:")
for row in result:
    print(*row)
