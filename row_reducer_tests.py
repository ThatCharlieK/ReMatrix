import time

import row_reducer
test_1 = [[8, 2, 3, 4, 7],
          [5, 3, 7, 8, 5],
          [7, 6, 2, 2, 3],
          [7, 9, 2, 5, 2]]

if __name__ == "__main__":

    start_time = time.time()
    stored_test = [row[:] for row in test_1]
    row_reducer.row_reduce_matrix(test_1)
    row_reducer.analyze_row_reduced_matrix(test_1, stored_test)
    solutions = row_reducer.get_matrix_solutions(test_1)
    row_reducer.print_solution_set(solutions)

    print(row_reducer.check_solution_set(stored_test, solutions))
    print(f"Took {time.time() - start_time} seconds to compute matrix")