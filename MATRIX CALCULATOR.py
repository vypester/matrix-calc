#MATRIX CALCULATOR

#Functions

def matrix_setup(matrix_input_rows,matrix_input_columns):
    row = []
    column = []
    for i in range(matrix_input_rows):
        for j in range(matrix_input_columns):
            value = input(f"Input Column {j+1}, Row {i+1}'s Value:")
            row.append(int(value))
        column.append(row)
        row = []
    return column

def matrix_print(matrix_input_rows, matrix_number):
    for i in range(matrix_input_rows):
        print(matrix_number[i])
    return

def matrix_addition(matrix_1, matrix_2, matrix_columns, matrix_rows):
    for i in range(matrix_rows):
        for j in range(matrix_columns):
            matrix_1[i][j] = (matrix_1[i][j] + matrix_2[i][j])
    return matrix_1

def matrix_multiplication(matrix_1_rows, matrix_2_columns, matrix_2_rows):
    value = 0
    row = []
    column = []
    for i in range(matrix_1_rows):
        for k in range(matrix_2_columns):
            for j in range(matrix_2_rows):
                value += (matrix_1[i][j] * matrix_2[j][k])
            row.append(value)
            value = 0
        column.append(row)   
        row = []
    return column


def determinant_2x2(matrix_2x2):
    value = matrix_2x2[0][0] * matrix_2x2[1][1] - matrix_2x2[0][1] * matrix_2x2[1][0] 
    return value

def matrix_determinant(matrix_rows, matrix):
    row = []
    column = []
    submatrix = []
    number = 0
    i = 1
    j = 0
    k = 0
    while k < matrix_rows:
        while i < matrix_rows:
            while j < matrix_rows:
                if j == k:
                    j += 1
                    continue
                value = matrix[i][j]
                row.append(int(value))
                j += 1
            column.append(row)
            row = []
            i += 1
            j = 0
        submatrix.append(column)
        column = []
        k += 1
        i = 1
    #print(submatrix)
    i = 0

    if len(submatrix[0][0]) == 2:
        while j < matrix_rows:
            if (j+1) % 2 != 0:
                number += matrix[i][j] * determinant_2x2(submatrix[j])
            else:
                number -= matrix[i][j] * determinant_2x2(submatrix[j])
            j += 1
    else:
        for i in range(len(submatrix[0])+1):
            if (i+1) % 2 != 0:
                number += matrix[0][i] * matrix_determinant(len(submatrix[i]), submatrix[i])
            else:
                number -= matrix[0][i] * matrix_determinant(len(submatrix[i]), submatrix[i])

    return number


#Calculator

choice = int(input("Add or Multiply Matrices? Get Determinant? (1 for Add, 2 for Multiply, 3 for Determinant):"))



if choice == (1 or 2):
    M1_c = int(input("Matrix 1 Columns:"))
    M1_r = int(input("Matrix 1 Rows:"))
    M2_c = int(input("Matrix 2 Columns:"))
    M2_r = int(input("Matrix 2 Rows:"))

    matrix_1 = matrix_setup(M1_r, M1_c)
    matrix_2 = matrix_setup(M2_r, M2_c)

#else:
    print("Error. Invalid number selection.")





#matrix_print(M1_r, matrix_1)
#matrix_print(M2_r, matrix_2)



#Addition

if choice == 1:
    
    if M1_r == M2_r and M1_c == M2_c:
        added_matrix = matrix_addition(matrix_1, matrix_2, M1_c, M1_r)
        matrix_print(M1_r, added_matrix)
    else:
        print("Addition failed. Matrices are not the same size.")



#Multiplication

if choice == 2:

    if M1_c == M2_r:
        multiplied_matrix = matrix_multiplication(M1_r, M2_c, M2_r)
        matrix_print(M1_r, multiplied_matrix)

    else:
        print("Multiplication failed. Matrix 1's columns do not match Matrix 2's rows.")

#Determinant

if choice == 3:

    M_c = int(input("Matrix Columns:"))
    M_r = int(input("Matrix Rows:"))

    if M_c == M_r:

        matrix = matrix_setup(M_r, M_c)
        matrix_print(matrix)
        
        determinant = matrix_determinant(M_r, matrix)
        #determinant = matrix_determinant(matrix)
        print(determinant)


    
    else:
        print("Determinant calculation failed. Matrix is not square. (Columns do not equal rows.)")

