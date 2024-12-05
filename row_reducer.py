import random

def row_reduce_matrix(matrix):
    if not is_matrix_rectangular(matrix):
        raise ValueError("Input matrix must be rectangular to perform row reduction.")

    for col in range(len(matrix[1])):
        for row in range(len(matrix)):
            # only row reduce the spot in the matrix if its not a leading zero and its not zeroed already
            if row != col and matrix[row][col] != 0:
                zero_value_with_reduction(matrix, row, col)
    reduce_rows_to_lowest_terms(matrix)


def zero_value_with_reduction(matrix, row, col):
    """
    Zeros value at matrix[row][col] using the others rows in the matrix using reduction
    """
    if matrix[row][col] == 0:
        return
    # To zero the matrix[row] row, find another row to subtract from it
    for i in range(len(matrix)):
        # all values to the left of col in the selected row need to be 0s
        if matrix[i][col] != 0 and i != row and all(x == 0 for x in matrix[i][:col]):
            stored_list = matrix[i]
            # multiply both rows together so that matrix[row][col] = matrix[i][col]
            factor1 = matrix[i][col]
            factor2 = matrix[row][col]
            multiply_row(matrix, row, factor1)
            multiply_row(matrix, i, factor2)
            subtract_row_a_from_b(matrix, i, row)
            matrix[i] = stored_list # reset the row to the lowest form
            return


def reduce_rows_to_lowest_terms(matrix):
    """
    Reduces the row so that at least one of the terms is 1
    E.g [5, 0, 0, 15] -> [1, 0, 0, 3]
    :param matrix:
    :return:
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            # divide each row by the first term in the row
            if matrix[r][c] != 0:
                divide_row(matrix, r, matrix[r][c])
                break


def multiply_row(matrix, row, factor):
    matrix[row] = [item * factor for item in matrix[row]]


def divide_row(matrix, row, divisor):
    matrix[row] = [item / divisor for item in matrix[row]]


def add_row_a_to_b(matrix, row_a_number, row_b_number):
    matrix[row_b_number] = [a + b for a, b in zip(matrix[row_a_number], matrix[row_b_number])]


def subtract_row_a_from_b(matrix, row_a_number, row_b_number):
    matrix[row_b_number] = [b - a for a, b in zip(matrix[row_a_number], matrix[row_b_number])]


def is_matrix_rectangular(matrix):
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            return False
    return True


def print_aligned_matrix(matrix):
    print("------------------")
    # Determine the maximum width of each column
    col_widths = []
    for col in range(len(matrix[0])):
        # a list representing the length of each item in the column
        col_lengths = (len(str(row[col])) for row in matrix)
        # the column is as wide as the largest item
        col_widths.append(max(col_lengths))

    # Print each row with the columns aligned
    for row in matrix:
        formatted_row = "  ".join(f"{str(item).rjust(width)}" for item, width in zip(row, col_widths))
        print(formatted_row)
    print("------------------")


def create_test_matrix(width, height, min, max):
    """
    :param width: the width of the resulting matrix
    :param height: the height of the resulting matrix
    :param min: the minimum value an item in the matrix can be
    :param max: the maximum value an item in the matrix can be
    :return: a width * height matrix
    """
    result = []
    for h in range(height):
        row = []
        for w in range(width):
            row.append(random.randint(min, max))
        result.append(row)
    return result

