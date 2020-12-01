

def initializeMatrix(n):
    matrix= [[[0] for i in range(0,n)] for j in range(0,n)]
    return matrix

def add(M1, M2, n):
    temp = [[0 for i in range(n)] for _ in range(n)]
    for i in range (0, n):
        for j in range(0, n):
            temp[i][j] = M1[i][j] + M2[i][j]
    return temp


def square_matrix_multiply(A,B,n):
    n = len(A)
    C = initializeMatrix(n)
    k= n//2

    if n == 1:
        C[0][0]= A[0][0] * B[0][0]
    else:
        A11 = initializeMatrix(k)
        A12 = initializeMatrix(k)
        A21 = initializeMatrix(k)
        A22 = initializeMatrix(k)
        B11 = initializeMatrix(k)
        B12 = initializeMatrix(k)
        B21 = initializeMatrix(k)
        B22 = initializeMatrix(k)

        for i in range(0, k):
            for j in range(0, k):
                A11[i][j] = A[i][j]
                A12[i][j] = A[i][k+j]
                A21[i][j] = A[k+i][j]
                A22[i][j] = A[k+i][k+j]
                B11[i][j] = B[i][j]
                B12[i][j] = B[i][k+j]
                B21[i][j] = B[k+i][j]
                B22[i][j] = B[k+i][k+j]
        C11 = add(square_matrix_multiply(A11, B11,k) , square_matrix_multiply(A12, B21,k) , k)
        C12 = add(square_matrix_multiply(A11, B12, k) , square_matrix_multiply(A12, B22, k), k)
        C21 = add(square_matrix_multiply(A21, B11, k) , square_matrix_multiply(A22, B21, k), k)
        C22 = add(square_matrix_multiply(A21, B12, k), square_matrix_multiply(A22, B22, k),k)

    for i in range(0, k):
        for j in range(0, k):
            C[i][j] = C11[i][j]
            C[i][j+k] = C12[i][j]
            C[k+i][j] = C21[i][j]
            C[k+i][k+j] = C22[i][j]


    return C

a2= [[1,2],[2,4]] #2x2 matrix
b2= [[3,2], [5,4]] #2x2 matrix
a4=[[1,2,3,4],[5,6,7,8],[4,3,2,1],[8,7,6,5]] #4x4 matrix
b4=[[1,2,3,4],[5,6,7,8],[4,3,2,1],[8,7,6,5]] #4x4 matrix
print(square_matrix_multiply(a2, b2, 2))
print(square_matrix_multiply(a4, b4, 4))


