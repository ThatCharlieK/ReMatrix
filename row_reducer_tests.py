import row_reducer
if __name__ == "__main__":
    test_1 = row_reducer.create_test_matrix(5, 4, -50, 50)
    row_reducer.print_aligned_matrix(test_1)
    row_reducer.row_reduce_matrix(test_1)
    row_reducer.print_aligned_matrix(test_1)