
# Transpose a matrix in a single line with user input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print(f"Enter elements row-wise:")
matrix = [[int(input()) for _ in range(cols)] for _ in range(rows)]
transpose = list(map(list, zip(*matrix)))
print("Transposed matrix:")
for row in transpose:
    print(row)
