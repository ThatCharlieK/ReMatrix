import random


def row_reduce_matrix(matrix):
    if not is_matrix_rectangular(matrix):
        raise ValueError("Input matrix must be rectangular to perform row reduction.")
    row_length = len(matrix[0])
    print("--- initial matrix ---")
    print_aligned_matrix(matrix)
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            # only row reduce the spot in the matrix if:
            # 1. it's not a leading zero
            # 2. it's not zeroed already
            # 3. It's not in the rightmost column (the right side of the equation
            if row != col and matrix[row][col] != 0 and col != row_length-1:
                zero_value_with_reduction(matrix, row, col)
            reduce_row_to_lowest_terms(matrix, row) # this line is optional, but prevents the matrix values from getting absurdley high
    print("--- row-reduced matrix ---")
    print_aligned_matrix(matrix)


def reduce_row_to_lowest_terms(matrix, row):
    for c in range(len(matrix[row])):
        if matrix[row][c] != 0:
            divide_row(matrix, row, matrix[row][c])
            break


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
        reduce_row_to_lowest_terms(matrix, r)


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


def get_matrix_solutions(matrix):
    solution_set = []
    for i in range(len(matrix)):
        if all(x == 0 for x in matrix[i][:-1] ):
            # when there is no solution from that line
            solution_set.append(None)
        else:
            solution_set.append(matrix[i][-1])
    return solution_set


def print_solution_set(solution_set):
    """
    :param solution_set: a solution set, such as the one returned by get_matrix_solutions
    :return: n/a
    """
    print("the solution set is: ")
    for i in range(len(solution_set)):
        print(f"x_{i} = {solution_set[i]}")


def analyze_row_reduced_matrix(row_reduced_matrix, original_matrix):
    solution_set = get_matrix_solutions(row_reduced_matrix)
    print_solution_set(solution_set)
    correct = check_solution_set(original_matrix, solution_set)
    if correct:
        print("The solution set solves the original matrix")
    else:
        print("The matrix cannot be solved")



def check_solution_set(original_matrix, solution_set):
    """
    :param original_matrix: The matrix that's not row-reduced
    :param solution_set: a list of [x_1, x_2, x_3...]
    :return:
    """
    def is_a_within_margin_of_b(a, b):
        margin_of_error = 0.00005
        return b + margin_of_error > a > b - margin_of_error

    for row in original_matrix:
        coefficients = row[:-1]
        row_sum = row[-1]
        dot = dot_product(coefficients, solution_set)
        if not is_a_within_margin_of_b(sum(dot), row_sum):
            return False
    return True


def dot_product(row_a, row_b):
    """
    e.g [a, b, c]  * [d, e, f] = [ad, be, fc]
    :param row_a:
    :param row_b:
    :return:
    """
    result = [a * b for a, b in zip(row_a, row_b)]
    return result
