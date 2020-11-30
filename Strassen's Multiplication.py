#conditions for strassen algo: matrix should be nxn where n=power of 2

def initializeMatrix(n):
    matrix= [[[0] for i in range(0,n)] for j in range(0,n)]
    return matrix

#add two matrixes of dimension n
def add(M1, M2, n):
    temp = initializeMatrix(n)
    for i in range (0, n):
        for j in range(0, n):
            temp[i][j] = M1[i][j] + M2[i][j]
    return temp

#add two matrixes of dimension n
def subtract(M1, M2, n):
    temp = initializeMatrix(n)
    for i in range (0, n):
        for j in range(0, n):
            temp[i][j] = M1[i][j] - M2[i][j]
    return temp

def strassen(A,B,n):
    # base case
    if (n == 1):
        C = initializeMatrix(n)
        C[0][0] = A[0][0] * B[0][0]
        return C
    
    # Declaring C and calculating dimension of sub-matrices
    C = initializeMatrix(n)
    k = int(n / 2)
    
    # Initializing sub-matrices and defining sub-matrices
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
    
    # Calculating the product P1 to P7 and the resulting matrix C using formulas
    P1 = strassen(A11, subtract(B12, B22, k), k)
    P2 = strassen(add(A11, A12, k), B22, k)
    P3 = strassen(add(A21, A22, k), B11, k)
    P4 = strassen(A22, subtract(B21, B11, k), k)
    P5 = strassen(add(A11, A22, k), add(B11, B22, k), k)
    P6 = strassen(subtract(A12, A22, k), add(B21, B22, k), k)
    P7 = strassen(subtract(A11, A21, k), add(B11, B12, k), k)

    C11 = subtract(add(add(P5, P4, k), P6, k), P2, k)
    C12 = add(P1, P2, k)
    C21 = add(P3, P4, k)
    C22 = subtract(subtract(add(P5, P1, k), P3, k), P7, k)

    #Copying values to C and returning C
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
print(strassen(a2, b2, 2))
print(strassen(a4, b4, 4))