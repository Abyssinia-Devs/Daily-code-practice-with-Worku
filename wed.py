def numSpecial(mat):
    m = len(mat)
    n = len(mat[0])
    special_count = 0

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                row_check = all(mat[i][k] == 0 for k in range(n) if k != j)

                col_check = all(mat[k][j] == 0 for k in range(m) if k != i)
                
                if row_check and col_check:
                    special_count += 1

    return special_count
                