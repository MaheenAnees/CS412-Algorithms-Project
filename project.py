
def square_matrix_multiply(A,B):
    n = len(A)
    C = [[0 for i in range(len(A))] for _ in range(len(B))]

    if n == 1:
        C[1][1] = A[1][1] * B[1][1]
    else:
        C[1][1] = square_matrix_multiply(A[1][1], B[1][1]) + square_matrix_multiply(A[1][2], B[2][1])
        C[1][2] = square_matrix_multiply(A[1][1], B[1][2]) + square_matrix_multiply(A[1][2], B[2][2])
        C[2][1] = square_matrix_multiply(A[2][1], B[1][1]) + square_matrix_multiply(A[2][2], B[2][1])
        C[2][2] = square_matrix_multiply(A[2][1], B[1][2]) + square_matrix_multiply(A[2][2], B[2][2])

    return C

    



