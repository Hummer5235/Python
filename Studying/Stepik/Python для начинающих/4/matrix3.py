def print_matrix(matrix, n, width=6):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


matrix  = [[277, -930, 11, 0],
           [9, 43, 6, 87],
           [4456, 8, 290, 7],
           [5, 0, 11, 24]]

print_matrix(matrix, 4)