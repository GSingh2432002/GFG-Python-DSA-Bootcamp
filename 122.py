# Rotate a Matrix
def rotate_matrix(matrix):
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse the columns
    for i in range(n):
        for j, k in zip(range(n//2), range(n-1, n//2-1, -1)):
            matrix[j][i], matrix[k][i] = matrix[k][i], matrix[j][i]
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(elem) for elem in row))

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print("Original matrix:")
print_matrix(matrix)
rotate_matrix(matrix)
print("Rotated matrix:")
print_matrix(matrix)