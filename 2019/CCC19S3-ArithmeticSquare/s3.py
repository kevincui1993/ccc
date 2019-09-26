import sys
import math

def check(m, r, c):
    return r >= 0 and r < 3 and c >= 0 and c < 3 and m[r][c] != 'X'

matrix = []
for i in range(3):
    row = sys.stdin.readline()
    matrix.append(row[:-1].split(' '))

count = 0
for i in range(3):
    for j in range(3):
        if matrix[i][j] != 'X':
            count += 1 
           
while count < 9:
    updated = False
    #print (matrix)
    #print(count)
    for i in range(3):
        if matrix[i].count('X') == 1:
            if matrix[i][0] == 'X':
                matrix[i][0] = str(2 * int(matrix[i][1]) - int(matrix[i][2])) 
            elif matrix[i][1] == 'X':
                matrix[i][1] = str(int((int(matrix[i][2]) - int(matrix[i][0])) /2) + int(matrix[i][0]))
            else:
                matrix[i][2] = str(2 * int(matrix[i][1]) - int(matrix[i][0]))
            updated = True
            count += 1
            break
        
        temp = [matrix[0][i], matrix[1][i], matrix[2][i]]
        if temp.count('X') == 1:
            if matrix[0][i] == 'X':
                matrix[0][i] = str(2 * int(matrix[1][i]) - int(matrix[2][i])) 
            elif matrix[1][i] == 'X':
                matrix[1][i] = str(int((int(matrix[2][i]) - int(matrix[0][i])) /2) + int(matrix[0][i]))
            else:
                matrix[2][i] = str(2 * int(matrix[1][i]) - int(matrix[0][i]))
            updated = True
            count += 1
            break
    if not updated:
        row_occupied,col_occupied = -1, -1
        for i in range(3):
            if matrix[i].count('X') == 0:
                row_occupied = i
            temp = [matrix[0][i], matrix[1][i], matrix[2][i]]
            if temp.count('X') == 0:
                col_occupied = i
                
        if row_occupied >= 0 and col_occupied >= 0:
            nrow,ncol = (row_occupied + 1) % 2, (col_occupied+1) % 2
            if check(matrix, nrow-1, ncol):
                if check(matrix, nrow, ncol-1):
                    matrix[nrow][ncol] = str(int(matrix[nrow][ncol-1]) - int(matrix[nrow-1][ncol-1]) + int(matrix[nrow-1][ncol]))
                else:
                    matrix[nrow][ncol] = str(int(matrix[nrow][ncol+1]) - int(matrix[nrow-1][ncol+1]) + int(matrix[nrow-1][ncol]))
            else:
                if check(matrix, nrow, ncol-1):
                    matrix[nrow][ncol] = str(int(matrix[nrow+1][ncol]) - int(matrix[nrow+1][ncol-1]) - int(matrix[nrow][ncol-1]))
                else:
                    matrix[nrow][ncol] = str(int(matrix[nrow+1][ncol]) - int(matrix[nrow+1][ncol+1]) - int(matrix[nrow][ncol+1])) 
            count+=1
        elif row_occupied >= 0:
            for i in range(3):
                if i != row_occupied:
                    matrix[i] = matrix[row_occupied]
            break
        elif col_occupied >= 0:
            for i in range(3):
                if i != col_occupied:
                    matrix[0][i] = matrix[0][col_occupied]
                    matrix[1][i] = matrix[1][col_occupied]
                    matrix[2][i] = matrix[2][col_occupied]
            break
        else:
            if count == 0:
                matrix = [['1','1','1'],['1','1','1'],['1','1','1']]
                break
            elif count == 1:
                for i in range(3):
                    for j in range(3):
                        if matrix[i][j] != 'X':
                            matrix = [[ matrix[i][j] for k in range(3) ] for l in range(3)]
                            break
            elif count == 2:
                r1,col1,r2,col2 = -1,-1,-1,-1
                for i in range(3):
                    for j in range(3):
                        if matrix[i][j] != 'X':
                            if r1 < 0:
                                r1,col1 = i,j
                            else:
                                r2,col2 = i,j
                
                if int(matrix[r2][col2]) % 2 == 1:
                    matrix[r1][(col1+1)%2] = str(int(matrix[r1][col1]) + 1) if int(matrix[r1][col1]) % 2 == 0 else matrix[r1][col1]
                else:
                    matrix[r1][(col1+1)%2] = str(int(matrix[r1][col1]) + 1) if int(matrix[r1][col1]) % 2 == 1 else matrix[r1][col1]
                count+=1
            else:
                if matrix[1][1] == 'X':
                    matrix[1][1] = matrix[1][2]
                else:
                    matrix[0][1] = matrix[1][1]
                count+=1
for i in range(3):
    print(matrix[i][0] + ' ' + matrix[i][1] + ' ' + matrix[i][2])
    ##print('{} {} {}'.format(matrix[i][0], matrix[i][1], matrix[i][2]))