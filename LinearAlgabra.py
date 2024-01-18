
def determine2x2(matrix):
    return matrix[0][0]*matrix[1][1]-matrix[1][0]*matrix[0][1]
def determine3x3(matrix):

    a1=[[matrix[1][1],matrix[1][2]],[matrix[2][1],matrix[2][2]]]
    a2=[[matrix[1][0],matrix[1][2]],[matrix[2][0],matrix[2][2]]]
    a3=[[matrix[1][0],matrix[1][1]],[matrix[2][0],matrix[2][1]]]

    return matrix[0][0]*determine2x2(a1)-matrix[0][1]*determine2x2(a2)+matrix[0][2]*determine2x2(a3)

# def inverse(matrix):
#     inverse=[[1,0,0],[0,1,0],[0,0,1]]
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             matrix[i][j]=matrix[i][j]/matrix[i][i]
#         for j in range(len(matrix)) :
#             a=matrix[(i+1)%3][1]/matrix[i][i]
#             matrix[(i+1)%3][j]=matrix[(i+1)%3][j]-a*matrix[i][j]
#             inverse[(i+1)%3][j]=inverse[(i+1)%3][j]-a*inverse[i][j]
#             a = matrix[(i + 2) % 3][1] / matrix[i][i]
#             matrix[(i + 2) % 3][j] -= matrix[(i + 2) % 3][j] - a * matrix[i][j]
#             inverse[(i+2)%3][j]=inverse[(i+2)%3][j]-a*inverse[i][j]
#     print(inverse)

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def inverse(matrix):
    det = determine3x3(matrix)

    if det == 0:
        raise ValueError("The matrix is singular, and its inverse does not exist.")

    cofactors = [[0, 0, 0] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            minor_matrix = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
            cofactors[i][j] = ((-1) ** (i + j)) * determine2x2(minor_matrix)

    adjugate = transpose(cofactors)

    inverse_matrix = [[adjugate[i][j] / det for j in range(3)] for i in range(3)]

    return inverse_matrix
def matrix_multiply(matrix_a, matrix_b):
    result = [[sum(a*b for a, b in zip(row_a, col_b)) for col_b in zip(*matrix_b)] for row_a in matrix_a]
    return result
def solve_linear_system(coefficients, constants):
    try:
        inv_coefficients = inverse(coefficients)
        solution = matrix_multiply(inv_coefficients, constants)
        return solution
    except ValueError as e:
        return str(e)
matrixA=[[1,0,0],
         [0,1,0],
         [0,0,1]]
matrixB=[[1,1],
         [2,2],
         [3,3]]

matrixC=matrix_multiply(matrixA,matrixB)
print(matrixC)
print(determine2x2([[1,2],[3,4]]))
print(transpose([[1,2,3],[4,5,6],[7,8,10]]))
print(inverse([[1,2,3],[4,5,6],[7,8,10]]))

coff=[
    [1,2,3],
    [2,5,3],
    [2,0,8]
]
constanse=[[10],[15],[20]]
print(solve_linear_system(coff, constanse))