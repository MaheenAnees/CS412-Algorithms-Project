

######################################## F I N A L ##########################################

# Program to multiply matrices using nested loops

def naive_matrix_mult(M1, M2, result):
# iterate through rows of M1
    for i in range(len(M1)):
       # iterate through columns of M2
       for j in range(len(M2[0])):
           # iterate through rows of M2
           for k in range(len(M2)):
               result[i][j] += M1[i][k] * M2[k][j]
    return result

def main():
    # 3x3 matrix
    M1 = [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]
    
    # 3x4 matrix
    M2 = [[5,8,1,2],
        [6,7,3,0],
        [4,5,9,1]]
        
    #Resulting matrix = 3 x 4
    Res = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]
        
    result = naive_matrix_mult(M1, M2, Res)
    for i in result:
        print(i)
        
main()
