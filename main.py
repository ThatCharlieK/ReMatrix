example_matrix = [[1, 1, 1, 1],
                  [1, 1, 1, 1],
                  [1, 1, 1, 1]]

matrix_to_solve = [[1, 3, 7, 2],
                   [7, 3, 1, 6],
                   [6, 5, 6, 1]]

step_2 =   [[1, 3, 7, 2],
            [0, 3, 1, 6],
            [0, 5, 6, 1]]



def row_reduce_matrix(matrix):
    if not is_matrix_rectangular(matrix):
        raise ValueError("Input matrix must be rectangular to perform row reduction.")

    for col in range(len(matrix[1])):
        for row in range(len(matrix)):
            # only row reduce the spot in the matrix if its not a leading zero and its not zeroed already
            if row != col and matrix[row][col] != 0:
                zero_value_with_reduction(matrix, row, col)


"""
Zeros value at matrix[row][col] using the others rows in the matrix using reduction
"""
def zero_value_with_reduction(matrix, row, col):
    if(matrix[row][col] == 0):
        return
    # To zero the matrix[row] row, find another row to subtract from it
    for i in range(len(matrix)):
        #
        if matrix[i][col] != 0 and i != row:
            stored_list = matrix[i]
            # multiply both rows together so that matrix[row][col] = matrix[i][col]
            factor1 = matrix[i][col]
            factor2 = matrix[row][col]
            multiply_row(matrix, row, factor1)
            multiply_row(matrix, i, factor2)
            subtract_row_a_from_b(matrix, i, row)
            matrix[i] = stored_list # reset the row to the lowest form
            return
        #aksjdfh

def multiply_row(matrix, row, factor):
    matrix[row] = [item * factor for item in matrix[row]]


def add_row_a_to_b(matrix, rowANumber, rowBNumber):
    matrix[rowBNumber] = [a + b for a, b in zip(matrix[rowANumber], matrix[rowBNumber])]


def subtract_row_a_from_b(matrix, row_a_number, row_b_number):
    matrix[row_b_number] = [b - a for a, b in zip(matrix[row_a_number], matrix[row_b_number])]


def is_matrix_rectangular(matrix):
    return True


print(matrix_to_solve)
zero_value_with_reduction(matrix_to_solve, 1, 0)
print(matrix_to_solve)
zero_value_with_reduction(matrix_to_solve, 2, 0)
print(matrix_to_solve)
# zero_value_with_reduction(matrix_to_solve, 0, 1)
# print(matrix_to_solve)
# zero_value_with_reduction(matrix_to_solve, 2, 1)
# print(matrix_to_solve)
# zero_value_with_reduction(matrix_to_solve, 0, 2)
# print(matrix_to_solve)
# zero_value_with_reduction(matrix_to_solve, 1, 2)
# print(matrix_to_solve)