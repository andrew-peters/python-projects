def rotate(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i + 1, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
            
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]   
    return matrix

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print()

matrix = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]]
printMatrix(matrix)

print("Rotated ->", end=" ")
print()
printMatrix(rotate(matrix))