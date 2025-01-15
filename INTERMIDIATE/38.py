def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter matrix:")
matrix = [[int(input(f"Element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

print("Transpose of the matrix:")
result = transpose(matrix)
for row in result:
    print(row)
