import row_reducer
test_1 = [[8, 2, 3, 4],
          [5, 3, 7, 8],
          [7, 9, 2, 5]]

if __name__ == "__main__":
    test_2 = row_reducer.create_test_matrix(100, 99, 1, 10)
    stored_test_2 = [row[:] for row in test_2]
    row_reducer.row_reduce_matrix(test_2)
    solutions = row_reducer.get_matrix_solutions(test_2)
    print(row_reducer.check_solution_set(stored_test_2, solutions))