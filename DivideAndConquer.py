def partition(X):
    x = len(X)
    y = len(X[0])
    a = [[0 for _ in range(x//2)] for _ in range(y//2)]
    b = [[0 for _ in range(x//2,x)] for _ in range(y//2)]
    c = [[0 for _ in range(x//2)] for _ in range(y//2, y)]
    d = [[0 for _ in range(x//2, x)] for _ in range(y//2,y)]

    for i in range(x//2):
        for j in range(y//2):
            a[i][j] = X[i][j]
    k = 0
    l = 0
    for i in range(x//2, x):
        for j in range(y//2):
            b[k][l] = X[i][j]
            l +=1
        k +=1
    k = 0
    l = 0
    for i in range(x//2):
        for j in range(y//2, y):
            c[k][l] = X[i][j]
            l +=1
        k +=1

    k = 0
    l = 0       
    for i in range(x//2, x):
        for j in range(y//2, y):
            d[k][l] = X[i][j]
            l +=1
        k +=1
            
    
    return a , b, c,d

def add(M1, M2, n):
    temp = [[0 for i in range(n)] for _ in range(n)]
    for i in range (0, n):
        for j in range(0, n):
            temp[i][j] = M1[i][j] + M2[i][j]
    return temp


def square_matrix_multiply(A,B,n):
    n = len(A)
    C = [[0 for i in range(n)] for _ in range(n)]
    k= n//2

    if n == 1:
        C[0][0]= A[0][0] * B[0][0]
        # return  C
    else:
        A11 , A12, A21, A22 = partition(A)
        B11 , B12, B21, B22 = partition(B)
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

f = [[1,2],[2,3]]
g =[[1,2],[1,2]] 
print(square_matrix_multiply(f,g,2))


