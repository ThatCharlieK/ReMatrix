# RowReducer
This library row takes a matrix and row reduces it. For example, the following code reduces an example matrix.
```py
import row_reducer
example_matrix = [[8, 2, 3, 4],
          [5, 3, 7, 8],
          [7, 9, 2, 5]]
row_reducer.row_reduce_matrix(example_matrix)
print(example_matrix)
```


It will turn it to row reduced form:
```math
[ 1  0  0  0.0620915032679738  ]
[ 0  1  0  0.2908496732026147  ]
[ 0  0  1  9738562091503268    ]
```