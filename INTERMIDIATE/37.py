def matrix_addition(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter matrix 1:")
matrix1 = [[int(input(f"Element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
print("Enter matrix 2:")
matrix2 = [[int(input(f"Element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

print("Matrix addition result:")
result = matrix_addition(matrix1, matrix2)
for row in result:
    print(row)
